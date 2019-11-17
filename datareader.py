# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/OMNI_HRO_1MIN_64070.txt', skipfooter=0, sep="\s+",
 skiprows=68, parse_dates=[[0,1]], engine='python',
 names=['date','time','by','bz',"flow pressure", "1-M_AE", "PC"],
 na_values={'by': 9999.99,'bz':9999.99,'FLOW_PRESSURE':99.9900,'1-M_AE':99.9900})
n = len(df["by"])-2
print(n )
t = np.linspace(0,24,n)
by = np.zeros(n)
bz = np.zeros(n)
FLOW_PRESSURE = np.zeros(n)
AE = np.zeros(n)
PC = np.zeros(n)

counter =-2
for i in range(n):
    print("time:",df["date_time"][i],)
    print("by:",df["by"][i] )

    print("bz:",df["bz"][i])
    print("FLOW_PRESSURE:", df["flow pressure"][i],)
    print("AE-index:", df["1-M_AE"][i])
    print("PC:",df["PC"][i])
    print("\n")
    if df["bz"][i]!=9999.99:
        by[i] = df["by"][i]
    if df["by"][i]!=9999.99:
        bz[i] = df["bz"][i]
    if df["flow pressure"][i]!=99.9900:
        FLOW_PRESSURE[i] = df["flow pressure"][i]
        print("I can't believe you have done this")

    AE[i] = df["1-M_AE"][i]
    PC[i] = df["PC"][i]

FLOW_PRESSURE=FLOW_PRESSURE[FLOW_PRESSURE !=0]
tflow = np.linspace(0,24,len(FLOW_PRESSURE))
print("counter",counter)
plt.plot(t,bz)
plt.title("bz")
plt.show()
plt.plot(t,by)
plt.title("by")
plt.show()
plt.plot(tflow, FLOW_PRESSURE)
plt.title("FLOW_PRESSURE")
plt.show()
plt.plot(t,AE)
plt.title("AE_index")
plt.show()
plt.plot(t,PC)
plt.show()

"""
plt.figure()
plt.subplot(3,1,1)
plt.plot(t,df['by'][2:])
plt.ylabel('By [nT]')
plt.gca().axes.xaxis.set_ticklabels([])
plt.subplot(3,1,2)
plt.plot(t,df['bz'][2:])
plt.ylabel('Bz [nT]')
plt.gca().axes.xaxis.set_ticklabels([])
plt.subplot(3,1,3)
plt.plot(t,df['flow pressure'][2:i])
plt.ylabel('flow pressure [nPa]')
plt.gca().axes.xaxis.set_ticklabels([])
plt.show()
plt.plot(t, df['1-M_AE'][2:])
plt.ylabel('pdyn [nPa]')
plt.xlabel("data_time")
plt.show()
"""
