import numpy as np

def true_val():
    return 0.397887
def true_func(params):
  x1 = params['x']
  x2 = params['y']
  a = 1
  b = 5.1/(4*np.pi**2)
  c = 5/np.pi
  r = 6
  s = 10
  t = 1/(8*np.pi)

  f  = a*(x2 - b*x1**2 +c*x1 - r)**2 + s*(1-t)*np.cos(x1) + s
  c1 = 2. - a*(x2 - b*x1**2 + c*x1 - r)**2

  return {'f':f, 'c1':c1}
