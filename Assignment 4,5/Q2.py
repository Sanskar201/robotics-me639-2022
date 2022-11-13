import numpy as np
#Link lengths:
l1=4
l2=3
l3=2
#Enter the position of end effector here:
P=np.array([-4.732050807568878, -1, 3])
Px,Py,Pz=P
theta_2=np.arccos((Px**2+Py**2-l2**2-l3**2)/(2*l2*l3))
theta_1=np.arctan2(l3*np.sin(theta_2)*Px+(l2+l3*np.cos(theta_2))*Py,(l2+l3*np.cos(theta_2))*Px-l3*np.sin(theta_2)*Py)
theta_1=-np.arctan2(Px,Py)+np.arctan2(l2+l3*np.cos(theta_2),l3*np.sin(theta_2))
d4=l1-Pz
print("theta_1 =",round(theta_1*180/np.pi,2))
print("theta_2 =",round(theta_2*180/np.pi,2))
print("d4 =",round(d4,2))