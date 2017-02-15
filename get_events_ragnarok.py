#importing the csv,regular expression modules
import csv
#from pprint import pprint
from datetime import datetime
import numpy as np
#events class
start_datetime = datetime.strptime('2011/10/20 11:58:32.623', '%Y/%m/%d %H:%M:%S.%f')
#frequency
freq = 12000
#seeting the time before and after events
time_before_event=2
time_after_event=3
#events class
class event:
    def __init__(self,timestamp,device,phase):
        self.date_time = (datetime.strptime(timestamp[:23], '%m/%d/%Y %H:%M:%S.%f') - start_datetime).total_seconds()
        self.phase=phase
        self.device=device
        self.file_num=0
        self.line_num=0

    def __str__(self):
        return 'Dno=%3s datetime=%12s P=%c Fno=%3d lno%8d'%(self.device,self.date_time,self.phase,self.file_num,self.line_num)

events=[]
#opening the csv file and referring  it with the variable f
with open("location_001_eventslist.txt","r") as datafile:
    #skipping the first line that contains the headers
    datafile.readline()
    #reading the contents of the file and serepating each line with a delimmiter 'COMMA'
    lines = csv.reader(datafile,delimiter=',')
    #printing words one by one from each line of the csvfile lines
    for line in lines:
            events.append(event(line[0],line[1],line[2]))

#Printing the extracted events
print 'Here are the extracted events'
for e in events:
    print e
count = 0

for i in xrange(401,801):
    with open ('location_001_ivdata_%003d.txt'%i,'r') as f:
        #skipping the first 24 lines (headers)
        for x in xrange(24):
            f.readline()
        #saving the position and reading the first line
        pos,a = f.tell(),float(f.readline().split(',')[0])
        #Readoing the last line of the file
        f.seek(-80,2)
        b=''
        while True:
            c = f.readline()
            if len(c)==0:
                break
            b=c
        b=float(b.split(',')[0])
        print "File=%003d START=%00005d END=%00005d EVENT=%00005d" %(i,int(a),int(b),int(events[count].date_time))
        while events[count].date_time > a and events[count].date_time < b:


            if b - events[count].date_time < 3:
                new_f = np.loadtxt('location_001_ivdata_%003d.txt'%(i+1),skiprows = 24,delimiter = ',')
                f = np.loadtxt('location_001_ivdata_%003d.txt'%i, skiprows = 24, delimiter = ',')
                data = np.concatenate((f,new_f))
                start, end = freq*int(events[count].date_time-a-time_before_event),freq*int(events[count].date_time-a+time_after_event)
                data = data[start:end]
                np.savetxt("events/{}_{}".format(events[count].device,events[count].date_time),data,delimiter=',')
            else:

            #get back to the first position
                f.seek(pos)
                data = np.loadtxt(f, delimiter=',')
                max_limit = len(data)
                start,end = freq*int(events[count].date_time-a-time_before_event),freq*int(events[count].date_time-a+time_after_event)
                start = start if start>0 else 0
                np.savetxt("events/{}_{}".format(events[count].device,events[count].date_time),data[start:end],delimiter=',')
            count+=1
            if count == max_limit:
                break
            print "ST=%000006d END=%0000006d LEN=%0000006d Max_LEN=%0000006d" %(start,end,end-start,max_limit)
print count
