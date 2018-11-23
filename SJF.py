a = []
burst_time=[]
waiting_time=[]
total_waiting_time=0
n = int(raw_input('Enter the total no of processes: '))
atime=(int(raw_input('Enter aival time: ')))
for i in xrange(n):
    a.append([])
    a[i].append(int(raw_input('Enter process number: ')))
    #pbust = 
    burst_time.append(int(raw_input('Enter burst time: ')))
j=1
for i in xrange(n):
    p=i
    for j in xrange(n):
        if burst_time[j]<burst_time[p]:
            p=j
        temp=burst_time[i]
        burst_time[i]=burst_time[p]
        burst_time[p]=temp
        temp=a[i]
        a[i]=a[p]
        a[p]=temp
waiting_time.append(0)
j=0
for i in xrange(n):
    waiting_time.append(0)
    for j in xrange(i):
        waiting_time[i]+=burst_time[i]
    total_waiting_time+=waiting_time[i]
print 'ProcessNumber\taivalTime\tBurstTime\tWaiting Time'
for i in xrange(n):
    print a[i],'\t\t',atime,'\t\t',burst_time[i], '\t\t',waiting_time[i]
    
print 'Total waiting time: ',total_waiting_time
print 'Average waiting time: ',(total_waiting_time/n)
