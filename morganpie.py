import numpy as np

k=1000
a = np.random.default_rng().uniform(-1.0, 1.0, (k, 2))
n=0
for x, y in a:
    if (x*x+y*y<=1):
        n+=1
print('Number of dots inside of circle: ', n ,'Pi = ', n/k*4)
