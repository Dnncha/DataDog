from get_data import *

def closing_lastn(n):
    """Closing price for the last n days"""
    data=get_data()
    dlen=len(data) #length of data (days)
    cp=data.Close[dlen-n:dlen] # closing price last n days
    return cp

