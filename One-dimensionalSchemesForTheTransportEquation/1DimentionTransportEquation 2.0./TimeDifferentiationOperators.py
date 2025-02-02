#-MODULES-AND-LIBRARYS-
import numpy              as np
import scipy

from scipy                import sparse
from scipy.sparse         import linalg
from numpy                import pi, sin, cos, ma, sqrt
from pylab                import *
#----------------------------------------------------------------------------------------#
#-------------------------------------BEGIN----------------------------------------------#
#----------------------------------------------------------------------------------------#
#-MAIN-CLASS-
class TimeDiff:
    
    #main methods
    def __init__(self, tmax, ct, space_operator): 
        self.tau            = tmax/ct
        self.v              = space_operator.v
        self.space_operator = space_operator
        
    def make_step(self, f):
        #один шаг по времени
        return f
        
    def diff(self, f):
        #полное дифференцирование по времени
        for j in range(f[:,0].size-1):
            f[j+1,:] = self.make_step(f[j,:])

#-CHILD-CLASES- 
class Euler(TimeDiff):

    def make_step(self, f):
        return f - self.tau*self.space_operator.diff(f)

class RK2(TimeDiff):

    def make_step(self, f):
        f1 = -self.space_operator.diff(f)
        f2 = -self.space_operator.diff(f1)
        return f + self.tau*f1 + self.tau**2/2*f2

class RK3(TimeDiff):

    def make_step(self, f):
        f1 = -self.space_operator.diff(f)
        f2 = -self.space_operator.diff(f1)
        f3 = -self.space_operator.diff(f2)
        return f + self.tau*f1 + self.tau**2/2*f2 + self.tau**3/6*f3

class RK4(TimeDiff):

    def make_step(self, f):
        f1 = -self.space_operator.diff(f)
        f2 = -self.space_operator.diff(f1)
        f3 = -self.space_operator.diff(f2)
        f4 = -self.space_operator.diff(f3)
        return f + self.tau*f1 + self.tau**2/2*f2 + self.tau**3/6*f3 + self.tau**4/24*f4

class RK5(TimeDiff):

    def make_step(self, f):
        f1 = -self.space_operator.diff(f)
        f2 = -self.space_operator.diff(f1)
        f3 = -self.space_operator.diff(f2)
        f4 = -self.space_operator.diff(f3)
        f5 = -self.space_operator.diff(f4)
        return f + self.tau*f1 + self.tau**2/2*f2 + self.tau**3/6*f3 + self.tau**4/24*f4 + self.tau**5/120*f5

class RK6(TimeDiff):

    def make_step(self, f):
        f1 = -self.space_operator.diff(f)
        f2 = -self.space_operator.diff(f1)
        f3 = -self.space_operator.diff(f2)
        f4 = -self.space_operator.diff(f3)
        f5 = -self.space_operator.diff(f4)
        f6 = -self.space_operator.diff(f5)
        return f + self.tau*f1 + self.tau**2/2*f2 + self.tau**3/6*f3 + self.tau**4/24*f4 + self.tau**5/120*f5 + self.tau**6/720*f6