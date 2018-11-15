import numpy as np
import math

def rosen(x, y):
    a = 1
    b = 100
    result = np.square(a - x) + b*np.square((y - np.square(x)))
    
    result = float(result)
    
    print 'Result = %f' % result
    #time.sleep(np.random.randint(60))
    return result
    
    # Write a function like this called 'main'
def main(job_id, params):
    print 'Anything printed here will end up in the output directory for job #%d' % job_id
    print params
    return rosen(params['x'], params['y'])

