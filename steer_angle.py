import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#list for angles
Hav=[]
sav=[]

#function keyboard input
def inputav():
    sa = input("Please enter Angle value in degree: \n")
    sa=float(sa)
    V = input("Please enter Speed value in m/s: \n")
    V=float(V)

    return sa, V
    
#function for heading angle
def Head_angle(sa,V,L):
    Ha=(V/L)*np.arctan(sa)
    Ha=np.rad2deg(Ha)  
    return Ha

#Car parameters
L=1.3 #m


while True:
    #import functions
    sa,V=inputav()
    Ha =Head_angle(np.deg2rad(sa),V,L)
    #add calculations to its lists
    Hav.append(Ha)
    sav.append(sa)
    print("Steering Angle= {}, Heading Angle= {}".format(sa,Ha))
    print(sav,Hav)

    #while loop interrupt
    i = input('Please enter \'Y\' or \'N\': ')
    if i.strip() == 'Y':
        break

#plot results
fig, ax = plt.subplots(1,1)
fig.set_figheight(8)
fig.set_figwidth(15)
fig.suptitle('Angle')
ax.plot(sav,'-',label="Steering Angle")
ax.plot(Hav,'-',label="Heading Angle")
ax.set(xlabel='# Samples', ylabel='Angle[°]')
ax.legend(loc="upper right")

plt.show()