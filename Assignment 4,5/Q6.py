import numpy as np
#The following code will work if the rotation matrices are multiplied in order R_z*R_y*R_x
#Enter the rotation matrix here:
R=np.array([[0.35355, -0.57322, 0.7392 ],
            [0.61237,   0.7392, 0.28033],
            [-0.7071,  0.35355, 0.61237]])
if round(np.linalg.det(R),2)!=1:
    print("The determinant of rotation matrix is not 1 ",(np.linalg.det(R),2))
    
else:
    q1=np.arctan2(R[1][0],R[0][0])
    q2=np.arcsin(-R[2][0])
    q3=np.arctan2(R[2][1],R[2][2])
    print("q1 =",round(q1*180/np.pi,2))
    print("q2 =",round(q2*180/np.pi,2))
    print("q3 =",round(q3*180/np.pi,2))
        