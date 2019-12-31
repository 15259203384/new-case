import sys
import copy

c={'r':'t','f':'t'}
a=copy.deepcopy(c)
print(a)
del a['r']
print(a)
print(c)