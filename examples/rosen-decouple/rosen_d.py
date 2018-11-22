import f as objective
import c1 as constraint_one
import numpy as np

def main(*args):


  return {'f':objective.main(*args)['f'],
         'c1':constraint_one.main(*args)['c1'],
         }


"""
Everything below this point is optional. It is used to specify
the true solution so that one can plot the error curve using 
progress_curve.py in the visualizations/ directory.
"""
def true_val():
    return 0
def true_func(job_id, params):
  x1 = params['x']
  x2 = params['y']
  a = 1
  b = 100
  

  c1 = -x1**2 - (x2-1)**2/2 + 2
  f  = (a - x1)**2 + b*(x2 - x1**2)**2
  return {'f':f, 'c1':c1}
