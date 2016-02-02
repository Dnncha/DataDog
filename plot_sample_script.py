import matplotlib.pyplot
from closing_lastn import *

n=365*2
cp=closing_lastn(n) # closing price last n days
cp_mean=sum(cp)/len(cp) # mean price last n days
#cp_med =median(cp) # median price last n days
print "mean price last", n, "days:", cp_mean
#print "median price last", n, "days:", cp_med
print cp.plot(figsize=(15, 10))

