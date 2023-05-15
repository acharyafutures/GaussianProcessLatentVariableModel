import qml
from qml.kernels import matern_kernel
from qml.math import cho_solve
import numpy as np

#Regression coefficients
def regression_alpha(x_train,y_train,sigma):
    # kernel for training
    k=matern_kernel(x_train,x_train,sigma,order=0,metric='l1')
    #for lambda=1e-5
    k[np.diag_indices_from(k)]+=1e-5
    a = cho_solve(k,y_train)
#     print (a)
    return a

def regression_test(x_test,x_train,sigma):
    b = matern_kernel(x_test, x_train, sigma,order=0,metric='l1')
    return b