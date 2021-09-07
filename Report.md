--------------------------------------------------------------------------
--------------------------------------------------------------------------
Accumulate mean transmisson from R0 to R0:                             0.00
Accumulate mean transmisson from R0 to R1:                             85.00
Accumulate mean transmisson from R0 to R2:                             88.67
Accumulate mean transmisson from R0 to R3:                             62.78
Accumulate mean transmisson from R0 to R4:                             92.00
Accumulate mean transmisson from R0 to R5:                             324.22
Accumulate mean transmisson from R0 to R6:                             5.67
Accumulate mean transmisson from R0 to R7:                             59.44
Accumulate mean transmisson from R0 to R8:                             7.89
Accumulate mean transmisson from R0 to R9:                             11.33
Accumulate mean transmission time from R0 to all router:               329.78

# message from R0 to R5 take the longest time since R6 has 5 channel connect to it, every time R6's neighbour get a message they will broadcast it, so the number of message that R6 get from its neighbour will increase very large. this means channels around R6 get alot of contention and since R0 need to get the message on channel channel R6-R5(in order to deliver to R5) means the message have to wait for a big chunk of time untill it turn to be on the channel 
# mesage from R0 to R6 take the shortest amount of time since channel R0-R6 is only used to send message to and from R0 and R6 so really small contention here
--------------------------------------------------------------------------
--------------------------------------------------------------------------
Accumulate mean transmisson from R1 to R0:                             328.44
Accumulate mean transmisson from R1 to R1:                             0.00
Accumulate mean transmisson from R1 to R2:                             150.89
Accumulate mean transmisson from R1 to R3:                             2.33
Accumulate mean transmisson from R1 to R4:                             3.78
Accumulate mean transmisson from R1 to R5:                             175.56
Accumulate mean transmisson from R1 to R6:                             165.11
Accumulate mean transmisson from R1 to R7:                             156.67
Accumulate mean transmisson from R1 to R8:                             167.33
Accumulate mean transmisson from R1 to R9:                             808.11
Accumulate mean transmission time from R1 to all router:               890.89

# message from R1 to R9 take the longest time to transmit since it have to go through R6, as R6 get really high contention as explain above. message from R1 to R0 and R1 to R8 on another hand, transmited a lot faster since the message does have to go through R6, there maybe noticable contention on channel R3-R7 or most likely channels that are around R3(since there are 4 router around R3 so the channels around R3 are likely to have a lot of contention, just not as much as channels that are around R6), This explain why transission time from R1 to R2 and R1 to R7 is large. but most of the channels on the right hand side (R3-7,R7-8,R8-0) are relatively small. Therefore the contention resolve quickly. 
--------------------------------------------------------------------------
--------------------------------------------------------------------------
Accumulate mean transmisson from R2 to R0:                             188.67
Accumulate mean transmisson from R2 to R1:                             45.44
Accumulate mean transmisson from R2 to R2:                             0.00
Accumulate mean transmisson from R2 to R3:                             7.67
Accumulate mean transmisson from R2 to R4:                             52.44
Accumulate mean transmisson from R2 to R5:                             11.00
Accumulate mean transmisson from R2 to R6:                             26.44
Accumulate mean transmisson from R2 to R7:                             54.78
Accumulate mean transmisson from R2 to R8:                             65.89
Accumulate mean transmisson from R2 to R9:                             703.00
Accumulate mean transmission time from R2 to all router:               705.56
--------------------------------------------------------------------------
--------------------------------------------------------------------------
Accumulate mean transmisson from R3 to R0:                             47.33
Accumulate mean transmisson from R3 to R1:                             2.22
Accumulate mean transmisson from R3 to R2:                             5.56
Accumulate mean transmisson from R3 to R3:                             0.00
Accumulate mean transmisson from R3 to R4:                             8.89
Accumulate mean transmisson from R3 to R5:                             13.33
Accumulate mean transmisson from R3 to R6:                             16.67
Accumulate mean transmisson from R3 to R7:                             11.11
Accumulate mean transmisson from R3 to R8:                             19.00
Accumulate mean transmisson from R3 to R9:                             214.78
Accumulate mean transmission time from R3 to all router:               214.78

# since channel R3 receive a lot of message from other router, it have to prioritize other message before able to transmit it own message, when every message come from other router has been transmited, the channel has are no more congested and its message can freely transmit on the channel, so those message get transmit really fast
--------------------------------------------------------------------------
--------------------------------------------------------------------------
Accumulate mean transmisson from R4 to R0:                             321.00
Accumulate mean transmisson from R4 to R1:                             2.78
Accumulate mean transmisson from R4 to R2:                             193.78
Accumulate mean transmisson from R4 to R3:                             6.56
Accumulate mean transmisson from R4 to R4:                             0.00
Accumulate mean transmisson from R4 to R5:                             214.33
Accumulate mean transmisson from R4 to R6:                             208.56
Accumulate mean transmisson from R4 to R7:                             200.11
Accumulate mean transmisson from R4 to R8:                             210.78
Accumulate mean transmisson from R4 to R9:                             902.11
Accumulate mean transmission time from R4 to all router:               902.11
# since most message that sent to R9 have to go through either R5-R6-R9 or R7-R6-R9. therefore, messages has been queue up alo      
--------------------------------------------------------------------------
--------------------------------------------------------------------------
Accumulate mean transmisson from R5 to R0:                             593.00
Accumulate mean transmisson from R5 to R1:                             61.33
Accumulate mean transmisson from R5 to R2:                             4.00
Accumulate mean transmisson from R5 to R3:                             28.11
Accumulate mean transmisson from R5 to R4:                             68.00
Accumulate mean transmisson from R5 to R5:                             0.00
Accumulate mean transmisson from R5 to R6:                             11.67
Accumulate mean transmisson from R5 to R7:                             601.89
Accumulate mean transmisson from R5 to R8:                             610.22
Accumulate mean transmisson from R5 to R9:                             611.44
Accumulate mean transmission time from R5 to all router:               611.78
--------------------------------------------------------------------------
--------------------------------------------------------------------------
Accumulate mean transmisson from R6 to R0:                             4.44
Accumulate mean transmisson from R6 to R1:                             17.78
Accumulate mean transmisson from R6 to R2:                             13.33
Accumulate mean transmisson from R6 to R3:                             15.56
Accumulate mean transmisson from R6 to R4:                             25.56
Accumulate mean transmisson from R6 to R5:                             10.00
Accumulate mean transmisson from R6 to R6:                             0.00
Accumulate mean transmisson from R6 to R7:                             13.33
Accumulate mean transmisson from R6 to R8:                             21.11
Accumulate mean transmisson from R6 to R9:                             22.22
Accumulate mean transmission time from R6 to all router:               25.56

# I have stated that channel around R6 have a lot of congestion. Because of that, message generated from R6 never have a chance to be on the channel, also because we alway prioritize message that come from other channels. That mean R6 can only deliver its message when there is no more congestion(only R6 message on the channel). This is why I observe that 9 message from R6 are are delivered at the end of the stimulation with fix transmission time on each message 
--------------------------------------------------------------------------
--------------------------------------------------------------------------
Accumulate mean transmisson from R7 to R0:                             158.00
Accumulate mean transmisson from R7 to R1:                             261.56
Accumulate mean transmisson from R7 to R2:                             264.89
Accumulate mean transmisson from R7 to R3:                             3.33
Accumulate mean transmisson from R7 to R4:                             268.33
Accumulate mean transmisson from R7 to R5:                             1251.33
Accumulate mean transmisson from R7 to R6:                             7.22
Accumulate mean transmisson from R7 to R7:                             0.00
Accumulate mean transmisson from R7 to R8:                             9.44
Accumulate mean transmisson from R7 to R9:                             1263.78
Accumulate mean transmission time from R7 to all router:               1320.78

# since R7 go through R6-R9, R7-R6 and R6-R5. these are jammed channel that waiting time at the channel pump up the transmision time

--------------------------------------------------------------------------
--------------------------------------------------------------------------
Accumulate mean transmisson from R8 to R0:                             2.33
Accumulate mean transmisson from R8 to R1:                             59.22
Accumulate mean transmisson from R8 to R2:                             62.56
Accumulate mean transmisson from R8 to R3:                             16.89
Accumulate mean transmisson from R8 to R4:                             65.89
Accumulate mean transmisson from R8 to R5:                             337.67
Accumulate mean transmisson from R8 to R6:                             20.44
Accumulate mean transmisson from R8 to R7:                             14.22
Accumulate mean transmisson from R8 to R8:                             0.00
Accumulate mean transmisson from R8 to R9:                             12.44
Accumulate mean transmission time from R8 to all router:               337.67

# R8-R5 get large because message has to wait for large amount of time since, the weight on both channel R8-R6 and R6-R5 (6 and 5 respectively) are quite large
--------------------------------------------------------------------------
--------------------------------------------------------------------------
Accumulate mean transmisson from R9 to R0:                             3.89
Accumulate mean transmisson from R9 to R1:                             1494.22
Accumulate mean transmisson from R9 to R2:                             1420.00
Accumulate mean transmisson from R9 to R3:                             1422.11
Accumulate mean transmisson from R9 to R4:                             1501.78
Accumulate mean transmisson from R9 to R5:                             1415.22
Accumulate mean transmisson from R9 to R6:                             6.11
Accumulate mean transmisson from R9 to R7:                             1418.56
Accumulate mean transmisson from R9 to R8:                             36.22
Accumulate mean transmisson from R9 to R9:                             0.00
Accumulate mean transmission time from R9 to all router:               1501.78

total sucessfull multicast: 900


# Overall system : the amount of congestion on each channel is base on the route that is pre-compute by Dijkstra algo, and the weight of the channel(time took to deliver a message). For example, on channel R6-R8 there are not much traffic on this channel, but the time it take to transimt a message is the highest (6 ticks) making it overload of message. 

# many number of message have to cross 2 major bridge. One is R3-R2-R5-R6, the other is R3-R7-R8. The latter is a litle less stress because the weight is not too much (2+1+2). the former R3-R2-R5-R6 with total weight(4+3+5) is making the transmision tremendously slow. 

# especially with channel R2-R3, as large amount of messages that wait on this channel and long waiting time making this channel the most congested channel

# most routers cant transmit their message until end of the stimulation because they have to prioritize other message that come from other router. 

# router that have more channel attach to them will likely suffer huge congestion issue, because the more message the router receive, the more message get sent( but just only few of them are accepted at their destination) most of the message are useless and making those channel jammed

# For example  if R6 receive message from R7 with the intended destination is R9, R6 will then fload all the channel around it with the message(5 messages sent in total) but only R9 will accept it, which mean 4 other message are useless and making the channels jammed 

# channels around R6 and R3 are more congested than other