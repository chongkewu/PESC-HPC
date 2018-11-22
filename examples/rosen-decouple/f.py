import numpy as np
import numpy.random as npr
import sys
import math
import time

def main(job_id, params):
  x1 = params['x']
  x2 = params['y']
  a = 1
  b = 100

  f  = (a - x1)**2 + b*(x2 - x1**2)**2
  return {'f' : f}

# def true_func(job_id, params):
#   return toy(params['x'], params['y'])
# def true_val():
#     return 0.5998
# def true_sol():
#     return {'x' : 0.1954, 'y' : 0.4044}
    
