#importing the csv,regular expression modules
import csv
import pprint

#events class
def format_time(time):
    time=time.split(':')
    sec=time[2].split('.')
    time = [int(time[0]),int(time[1]),int(sec[0]),int(sec[1])]
    return time

class event:
    def __init__(self,timestamp,device,phase):
        self.date,self.time=timestamp.split(' ')
        self.time = format_time(self.time)
        self.phase=phase
        self.device=device
        self.file_num=0

    def __str__(self):
        return 'Device={} Date={} Time={} phase={}'.format(self.device,self.date,self.time,self.phase)

def getfilenum(i):
    file_num,_i = [0,0,0], list(str(i))
    len_i=len(_i)-1
    for n in xrange(3):
        if n > len_i:
            break
        file_num[2-n]= _i[len_i-n]
    file_num = ''.join( str(e) for e in file_num)
    return file_num

def event_occurred(t1,t2):
    t1=t1[:]
    t2=t2[:]
    if t1[0]==t2[0]:
        #print 'H:',t1,t2
        if t1[1]-t2[1]>=0 and t1[1]-t2[1]<=2:
            #print 'M:',t1,t2
            #raw_input()
            t1[2],t2[2]=t1[1]*60+t1[2],t2[1]*60+t2[2]
            if t1[2]-t2[2]<=90 and t1[2]-t2[2]>=0:
                print 'S:',t1,t2
                #raw_input()
                return True
    return False

events=[]
#opening the csv file and referring  it with the variable f
with open("location_001_eventslist.txt","rb") as datafile:
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
#raw_input()

count = 0
#getting the starting recording time for each file
for i in xrange(1,401):
    with open('location_001_ivdata_{}.txt'.format(getfilenum(i)),'rb') as datafile:
        for n in xrange(15):
            datafile.readline()
        date=datafile.readline()[5:]
        date=date[:10]
        time=datafile.readline()[5:]
        time=time[:12]
        time=format_time(time)
        #raw_input()
        for e in events:
            if event_occurred(e.time,time):
                e.file_num=i
                count+=1
print count,len(events)
