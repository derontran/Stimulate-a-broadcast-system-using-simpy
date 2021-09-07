import simpy
from scipy import stats



routing_table = [
                 [-1, 8, 8, 8, 8, 6, 6, 8, 8, 9],
                 [3, -1, 3, 3, 4, 3, 3, 3, 3, 3],
                 [3, 3, -1, 3, 3, 5, 5, 3, 3, 5],
                 [7, 1, 2, -1, 4, 2, 7, 7, 7, 7],
                 [3, 1, 3, 3, -1, 3, 3, 3, 3, 3],
                 [6, 2, 2, 2, 2, -1, 6, 6, 6, 6],
                 [0, 7, 5, 7, 7, 5, -1, 7, 7, 9],
                 [8, 3, 3, 3, 3, 6, 6, -1, 8, 6],
                 [0, 7, 7, 7, 7, 7, 7, 7, -1, 0],
                 [0, 6, 6, 6, 6, 6, 6, 6, 0, -1]
                ]
# use to see the contention on each router
def analysis():
  a = [0 for i in range(10)]
  for r in range(len(routing_table)):
    for c in range(len(routing_table[r])):
      temp = routing_table[r][c]
      if temp != -1 :
        a[temp]+=1 
  print (a)
NUM_ROUTER = 10
NUM_MESSAGE  = 10
result = [[[0 for i in range(NUM_ROUTER)] for j in range(NUM_ROUTER)] for k in range(NUM_ROUTER)]  # store mean transmit time of stations 
report = [[0 for i in range(NUM_ROUTER)]for j in range(NUM_ROUTER)] 
acc_total = [0 for i in range(NUM_ROUTER)] 
TIME_SPEND=0
NUM_REPORT_GEN=0
NUM_REPORT_GEN1=0
NUM_REPORT_GEN2=0
def generate_report(sender,msg_id):
  print("--------------------------------------------------------------------------")
  print("Performance report on router R{}".format(sender))
  print
  index =0 
#   mean=0
  total=0
  for receiver in result[sender][msg_id]:
    print("Message #{}, transmisson time from R{} to R{}:                     {}".format(msg_id,sender, index,receiver))
   #  mean+= receiver
    if receiver > total:
       total = receiver
    report[sender][index]+= receiver
    index+=1

  print
  print("Total transmission time:                                        {}".format(total))
  acc_total[sender]+= total

# this use to monitor the queue length as time goes by
class MonitoredResource(simpy.PriorityResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queue_l = []
        self.observe_t =[]
    def request(self, *args, **kwargs):
        self.queue_l.append(len(self.queue))
        self.observe_t.append(self._env.now)
        return super().request(*args, **kwargs)

    def release(self, *args, **kwargs):
        self.queue_l.append(len(self.queue))
        self.observe_t.append(self._env.now)        
        return super().release(*args, **kwargs)

class Msg():
  def __init__(self,origin, msg_id):
    self.origin = origin
    self.msg_id = msg_id
    self.visited = []
    self.num_visited = 0
    
class Router():
  id=0 
  def __init__(self,env,channels):
    self.env =env
    self.msg_queue= simpy.PriorityStore(env) 
    self.router_id = Router.id
    Router.id+=1
    self.num_msg_gen = 0 
    self.num_msg_received = 0
    self.channels = channels
    self.routers_last_received = []
    self.env.process(self.msg_generate())
    self.env.process(self.transmit())
    for channel in self.channels:
       self.env.process(self.receive_msg(channel)) # start receiving on every channels
   
    
    
  
  def generate_msg_inter_arrival(self):
    return stats.poisson.rvs(20)

  def receive_msg(self,channel):
   global NUM_REPORT_GEN 
   global NUM_REPORT_GEN1
   while self.num_msg_received < (NUM_ROUTER-1)*NUM_MESSAGE:  # we only receive this amount at each router 
      msg = channel.msg
      if msg is not None : 
         if routing_table[self.router_id][msg.origin] in channel.owner and self.router_id not in msg.visited:
            result[msg.origin][msg.msg_id][self.router_id] += (self.env.now - msg.sent_time) # record the time the router receive the message
            NUM_REPORT_GEN1+=1  # record total message received, accumulated by at all router  
    
            msg.visited.append(self.router_id) # add this router as visited 
            msg.num_visited+=1  # update number of router which has received this msg
            self.num_msg_received+=1
            channel.msg = None # reset msg on the channel
            if msg.num_visited == NUM_ROUTER-1:
               generate_report(msg.origin,msg.msg_id)
               NUM_REPORT_GEN+=1 
               
            else:
               Pitem = simpy.PriorityItem("P0",msg)
               yield self.msg_queue.put(Pitem)
      yield self.env.timeout(1)

  def msg_generate(self):
    msg_id =0
    while self.num_msg_gen < NUM_MESSAGE:
      yield self.env.timeout(self.generate_msg_inter_arrival())
      msg = Msg(self.router_id,msg_id)  # create and send by this router id
      msg_id +=1
      msg.visited.append(self.router_id)
      Pitem = simpy.PriorityItem("P1",msg)
      self.num_msg_gen+=1  
      yield self.msg_queue.put(Pitem)    
  def transmit(self):
    global NUM_REPORT_GEN2
    while True: 
      Pitem = yield self.msg_queue.get()
      msg = Pitem.item
      # if msg gen at origin, record sent time
      if msg.origin == self.router_id:  
        msg.sent_time = self.env.now
      # send to all neighbour
      for channel in self.channels:
         yield self.env.process(channel.transmit(self.router_id,Pitem))
         NUM_REPORT_GEN2+=1

   


class Channel():
   def __init__(self, env,owner, transmit_time):
      self.owner = owner
      self.env = env
      self.resource= MonitoredResource(self.env,capacity=1)
      self.last_sent = None 
      self.msg = None 
      self.transmission_time = transmit_time
   def transmit(self, router_id, Pmsg):
      with self.resource.request() as req:
         yield req
         yield self.env.timeout(self.transmission_time)
         
         self.msg = Pmsg.item

         self.last_sent = router_id
  
observe_t= []
queue_l = [[] for i in range(14)]
def observe(env,channels):
  while True:
    observe_t.append(env.now)
    for i in range(len(channels)): 
        queue_l[i].append(len(channels[i].resource.queue))
    yield env.timeout(1)
def runSim():
  env = simpy.Environment()
  chanel_R0_R6  = Channel(env,[0,6],4)
  chanel_R0_R8 = Channel(env,[0,8],2)
  chanel_R0_R9 = Channel(env,[0,9],3)
  chanel_R1_R3 = Channel(env,[1,3],1)
  chanel_R1_R4  = Channel(env,[1,4],2)
  chanel_R2_R3 = Channel(env,[2,3],4)
  chanel_R2_R5 = Channel(env,[2,5],3)
  chanel_R3_R4 = Channel(env,[3,4],3)
  chanel_R3_R7 = Channel(env,[3,7],2)
  chanel_R5_R6 = Channel(env,[5,6],5)
  chanel_R6_R7 = Channel(env,[6,7],3)
  chanel_R6_R8 = Channel(env,[6,8],6)
  chanel_R6_R9 = Channel(env,[6,9],2)
  chanel_R7_R8 = Channel(env,[7,8],1)
  channels = [
              chanel_R0_R6,
              chanel_R0_R8, 
              chanel_R0_R9,
              chanel_R1_R3, 
              chanel_R1_R4, 
              chanel_R2_R3,
              chanel_R2_R5, 
              chanel_R3_R4,
              chanel_R3_R7, 
              chanel_R5_R6, 
              chanel_R6_R7,
              chanel_R6_R8,
              chanel_R6_R9, 
              chanel_R7_R8
            ] 
  router = []
  router.append(Router(env,[chanel_R0_R6,chanel_R0_R8,chanel_R0_R9]))
  router.append(Router(env,[chanel_R1_R3,chanel_R1_R4]))
  router.append(Router(env,[chanel_R2_R3,chanel_R2_R5]))
  router.append(Router(env,[chanel_R1_R3,chanel_R2_R3,chanel_R3_R4,chanel_R3_R7]))
  router.append(Router(env,[chanel_R1_R4,chanel_R3_R4]))
  router.append(Router(env,[chanel_R2_R5,chanel_R5_R6]))
  router.append(Router(env,[chanel_R0_R6,chanel_R5_R6,chanel_R6_R7,chanel_R6_R8,chanel_R6_R9])) #
  router.append(Router(env,[chanel_R3_R7,chanel_R6_R7,chanel_R7_R8]))
  router.append(Router(env,[chanel_R0_R8,chanel_R6_R8,chanel_R7_R8]))
  router.append(Router(env,[chanel_R0_R9,chanel_R6_R9]))

  env.run()

  # this export image showing contention amount on each channel
  # print("Simulation end at: {} vs time spend {}".format(env.now,TIME_SPEND))
  # for channel in channels:
  #   channel_owner = channel.owner
  #   plt.figure()
  #   plt.step(channel.resource.observe_t,channel.resource.queue_l,where="post")
  #   plt.xlabel("time")
  #   plt.ylabel(f"queue length of channel R{channel_owner[0]}-{channel_owner[1]}")
  #   plt.savefig(f"R{channel_owner[0]}-{channel_owner[1]}")
  #   print
 
  
  for r in range(len(report)): 
     acc_mean =0
     print("--------------------------------------------------------------------------")
     print("--------------------------------------------------------------------------")
     for c in range(len(report[r])): 
         mean= report[r][c]/float(NUM_ROUTER-1) 
         print("Accumulate mean transmisson from R{} to R{}:                             {:.2f}".format(r,c,mean))
     print
     print("Accumulate mean transmission time from R{} to all router:               {:.2f}".format(r,acc_total[r]/(NUM_ROUTER-1)))
  print("total sucessfull multicast:",NUM_REPORT_GEN1 )
     
runSim()


analysis()
