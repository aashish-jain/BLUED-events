import csv
# f=int(raw_input("Enter the file number"))
# t1=float(raw_input("Enter the time in seconds "))
f=14
t1=1408
csvfile = open('data.csv',"wb")
write = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
with open("location_001_ivdata_%003d.txt"%f,"rb") as dfile:
    for i in xrange(23):
        dfile.readline()
    lines = csv.reader(dfile,delimiter=',')
    for line in lines:
        if float(line[0])-t1>=-2 and float(line[0])-t1<=4:
            write.writerow(line)
csvfile.close()
