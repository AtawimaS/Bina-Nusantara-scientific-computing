import numpy as np
from numpy.linalg import eig
a=np.array([[166 ,177 ,188 ],[142 ,148 ,150 ],[89 ,127 ,80]])
w,v=eig(a)
print("Eigen Value  = ",w)
print("Eigen Vector = ", v)




import numpy as np
def normalize(x):
    fac = abs(x).max()
    x_n = x/ x.max()
    return fac, x_n
x = np.array([1,1,1])
a=np.array([[166 ,177 ,188 ],[142 ,148 ,150 ],[89 ,127 ,80]])

for i in range (8):
    x = np.dot(a,x)
    lambda_1,x=normalize(x)

print("Eigen Value : ", lambda_1)
print("Eigen Vector : ",x)
