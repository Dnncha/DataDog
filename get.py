import Quandl
import numpy
import pandas 

# authtoken from tnorthey Quandl account allows >50 API pulls/day
data=Quandl.get("BCHARTS/BTCNCNY", authtoken="_opb5TgvB6AbCAsFB7XS")

print data

