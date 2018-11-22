import numpy as np
import numpy.random as npr
import sys
import math
import time

def main(job_id, params):
  x1 = params['x']
  x2 = params['y']
  a = 1
  b = 5.1/(4*np.pi**2)
  c = 5/np.pi 
  r = 6
  s = 10
  t = 1/(8*np.pi)

  f  = a*(x2 - b*x1**2 +c*x1 - r)**2 + s*(1-t)*np.cos(x1) + s
  return {'f' : f}

# def true_func(job_id, params):
#   return toy(params['x'], params['y'])
# def true_val():
#     return 0.5998
# def true_sol():
#     return {'x' : 0.1954, 'y' : 0.4044}
    
