import csv
import matplotlib.pyplot as plt
import numpy as np
from os import listdir
directory='/media/aashish/0C0091CC0091BCE0/BLUED-D1-1/events'
files=listdir(directory)
count=0
completed=False
while(completed==False):
    try:
        for f in files:
            plt.close('all')
            print(count,f)
            data = np.loadtxt(directory+'/'+f, delimiter=',')
            count+=1
            t,i1,i2,v=[],[],[],[]
            i = 0
            while(True):
                t.append(max(data[i:i+200,0]))
                i1.append(max(data[i:i+200,1]))
                i2.append(max(data[i:i+200,2]))
                v.append(max(data[i:i+200,3]))
                i+=200
                if (i == 59800):
                     break
            print(max(i1),max(i2),max(v),max(t))
            print(len(t),len(i1),len(i2),len(v))
            _f, axarr = plt.subplots(3, sharex=True)
            axarr[0].plot(t,i1)
            axarr[0].set_title('I1')
            axarr[1].plot(t,i2)
            axarr[1].set_title('I2')
            axarr[2].plot(t,v)
            axarr[2].set_title('V')
            _f.subplots_adjust(hspace=0.15,wspace=0.15,top=0.96,bottom=0.03,right=0.96,left=0.03)
            plt.draw()
            plt.show()
        completed=True
    except:
        print("Some error")
