# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 12:56:15 2017

@author: Aashish Jain
"""

import matplotlib.pyplot as plt
import numpy as np
from os import listdir

directory='/media/aashish/0C0091CC0091BCE0/BLUED-D1-1/events'
files=listdir(directory)
count=0
for f in files:
    print f
    data = np.loadtxt(directory+'/'+f, delimiter=',')
    t=data[:,0]
    i1=data[:,1]
    i2=data[:,2]
    v=data[:,3]
    plt.close('all')

    # Two subplots, the axes array is 1-d

    f, axarr = plt.subplots(3, sharex=True)
    axarr[0].plot(t,i1)
    axarr[0].set_title('I1')
    axarr[1].plot(t,i2)
    axarr[1].set_title('I2')
    axarr[2].plot(t,v)
    axarr[2].set_title('V')


    # Fine-tune figure; make subplots farther from each other.
    f.subplots_adjust(hspace=0.15,wspace=0.15,top=0.96,bottom=0.03,right=0.96,left=0.03)
    plt.draw()
    plt.show()
    # plt.pause(10)
    #raw_input()
