avail_time=[]
burst_time=[]
ar=[]
sum_waiting_times=0
sum_turnaround_times=0
n=int(raw_input("Enter number of Process : "))
i=0
while i<n:
	print  "For process :",i+1
	avail_time.append(int(raw_input("Enter arrival time of process :")))
	burst_time.append(int(raw_input("Enter burst time of process :")))
	ar.append(burst_time[i])
	i+=1

print "\n\nProcess\t|Turnaround Time| Waiting Time\n"
ar.append(99999)
time=0
remain=0
j=i   	
while remain!=n:
        smallest=j
	i=0        
	while i<n:
            if avail_time[i]<=time and ar[i]<ar[smallest] and ar[i]>0:
                smallest=i
            i+=1       
        ar[smallest]-=1
        if ar[smallest]==0:
            remain+=1
            endTime=time+1
            print smallest+1,"\t","\t",endTime-avail_time[smallest],"\t","\t",endTime-burst_time[smallest]-avail_time[smallest]
            sum_waiting_times+=endTime-burst_time[smallest]-avail_time[smallest]
            sum_turnaround_times+=endTime-avail_time[smallest]
    	time+=1
print "\nAverage waiting time = ",sum_waiting_times*1.0/n
print "Average Turnaround time = ",sum_turnaround_times*1.0/5
