import numpy as np
import matplotlib.pyplot as plt


#list for angles
Hav=[]
sav=[]
#Car parameters
L=1.3 #m

#function for heading angle
def Head_angle(L):
    # keyboard input
    sa = input("Please enter Angle value in degree: \n")
    V = input("Please enter Speed value in Km/h: \n")
    #convert string to float
    sa=float(sa)
    V=float(V) #km/h
    V=(5/18)*(V) #m/s
    #Heading angle calculaten
    Ha=(V/L)*np.arctan(np.deg2rad(sa))
    Ha=np.rad2deg(Ha)
    return Ha, sa

try:
    while True:
        #import function
        Ha,sa =Head_angle(L)
        #add calculations to its lists
        Hav.append(Ha)
        sav.append(sa)
        print("Steering Angle= {}, Heading Angle= {}".format(sa,Ha))
        print(sav,Hav)

except KeyboardInterrupt:
    pass

for i in range(len(Hav)):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar', xlim=(-180, 180))
    ax.set_theta_offset(.5*np.pi) # point the origin towards the top
    ax.set_thetamin(-180) # set the limits
    ax.set_thetamax(180)
    ax.set_thetagrids(range(-180,180, 30))
    ax.set_title('Steering vs. Heading', pad=-50) # add title and relocate negative value lowers the location

    arrsa = plt.arrow(np.deg2rad(sav[i]), 0, 0, 0.8, alpha = 0.5, width = 0.020,
                    edgecolor = 'black', facecolor = 'green', lw = 2, zorder = 5)

    arrha = plt.arrow(np.deg2rad(Hav[i]), 0, 0, 1, alpha = 0.5, width = 0.020,
                    edgecolor = 'black', facecolor = 'green', lw = 2, zorder = 5)

    plt.show()