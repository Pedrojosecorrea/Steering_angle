import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Hav=[]
sav=[]
def inputav():
    sa = input("Please enter Angle value in degree: \n")
    sa=float(sa)
    V = input("Please enter Speed value in m/s: \n")
    V=float(V)

    return sa, V

def Head_angle(sa,V,L):
    Ha=(V/L)*np.arctan(sa)
    Ha=np.rad2deg(Ha)  
    return Ha

#sa=[30,25,20,15,10,5,0,-5,-10,-15,-20,-25,-30] #°
#V=[1,1,1.2,1.5,1.8,2,3,2,1.8,1.5,1.2,1,1] #m/s
L=1.3 #m
#dt=0.5 #s
# for i in range(len(sa)):
#     Ha_r =Head_angle(np.deg2rad(sa[i]),V[i],L)
#     Ha=np.rad2deg(Ha_r)
#     Hav.append(Ha)
#     print("Heading Angle= {}".format(Ha))

while True:
    sa,V=inputav()
    Ha =Head_angle(np.deg2rad(sa),V,L)

    Hav.append(Ha)
    sav.append(sa)
    print("Steering Angle= {}, Heading Angle= {}".format(sa,Ha))
    print(sav,Hav)

    i = input('Please enter \'Y\' or \'N\': ')
    if i.strip() == 'Y':
        break

fig, ax = plt.subplots(1,1)
fig.set_figheight(8)
fig.set_figwidth(15)
fig.suptitle('Angle')
ax.plot(sav,'-',label="Steering angle")
ax.plot(Hav,'-',label="Heading Angle")
ax.set(xlabel='# samples', ylabel='Angle[°]')
ax.legend(loc="upper right")

plt.show()