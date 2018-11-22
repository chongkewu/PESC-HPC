import numpy as np

def true_val():
    return 0
def true_func(params):
  x1 = params['x']
  x2 = params['y']
  a = 1
  b = 100
  

  c1 = -x1**2 - (x2-1)**2/2 + 2
  f  = (a - x1)**2 + b*(x2 - x1**2)**2
  return {'f':f, 'c1':c1}
