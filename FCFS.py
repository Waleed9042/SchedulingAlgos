a = []
t = 0
total= int(raw_input('Enter the totalal no of processes: '))
for i in xrange(total):
    a.append([])
    a[i].append(raw_input('Enter process name: '))
    a[i].append(int(raw_input('Enter arrival time: ')))
    t += a[i][1]
    a[i].append(int(raw_input('Enter burst time: ')))

a.sort(key = lambda a:a[1])

print 'Name\tArrivalTime\tBurstTime'
for i in xrange(total):
    print a[i][0],'\t',a[i][1],'\t',a[i][2]
    
print 'Total waiting time: ',t
print 'Average waiting time: ',(t/total)
