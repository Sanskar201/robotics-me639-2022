import numpy as np
#Link lengths of first two links:
l1=3
l2=2
#Enter the position of end effector here:
P=np.array([-2, 0.866, 2.5])
Px,Py,Pz=P
r=np.sqrt(Px**2+Py**2)
s=Pz-l1
theta_1=np.arctan2(Py,Px)-np.arctan2(l2,np.sqrt(r**2-l2**2))
theta_2=np.arctan2(np.cos(theta_1)*Px+np.sin(theta_1)*Py,s)
d3=np.sin(theta_2)*(np.cos(theta_1)*Px+np.sin(theta_1)*Py)+np.cos(theta_2)*s

print("theta_1 =",round(theta_1*180/np.pi,2))
print("theta_2 =",round((theta_2-theta_1)*180/np.pi,2))
print("d3 =",round(d3,2))