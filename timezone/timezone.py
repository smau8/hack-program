#!/usr/bin/env python

"""
A function for displaying different timezones and calculating time differences within the US. 
"""

import datetime
from datetime import datetime
import pytz
from pytz import timezone
import pandas as pd

# global variables defined
REGIONS = ["westcoast", "midwest", "eastcoast"]
TIMEZONE_OUTPUT = {'region': [], 'current time':[]}
FMT = '%Y-%m-%d %H:%M:%S %Z%z'

# define timezones class
class timezones:
    def __init__(self, arg=0):
        # store final data
        self.data = pd.DataFrame(data=TIMEZONE_OUTPUT)

    def region(self, arg):
        """
        returns timezone facts
        """
        # print current location and hour difference between the three regions
        if arg == "westcoast":
            print("Current location: {}".format(arg))
            print("Your current time is 3 hours behind east coast and 2 hours behind midwest.")

        elif arg == "midwest":
            print("Current location: {}".format(arg))
            print("Your current time is 1 hour behind east coast and 2 hours ahead west coast.")
    
        elif arg == "eastcoast":
            print("Current location: {}".format(arg))
            print("Your current time is 3 hours ahead west coast and 1 hour ahead midwest.") 

    def time_diff(self, arg):
        """
        Set local time based on user input. 
        """
        if arg == "westcoast":
            arg_tz = timezone('America/Los_Angeles')
        if arg == "midwest":
            arg_tz = timezone('America/Chicago')
        if arg == "eastcoast":
            arg_tz = timezone('America/New_York')
        
        arg_dt = arg_tz.localize(datetime.now())
        local_time = arg_dt.strftime(FMT)
        temp_output = pd.DataFrame([[arg, local_time]], columns=['region', 'current time'])
        # store current location time data in final data frame
        print(temp_output)
        #self.data = self.data.append(temp_output)


        """
        Calculate time differences with other US regions
        """
        # remove local location indicated by user
        REGIONS.remove(arg)
        # use for loop to loop through the remaining locations
        for idx in REGIONS:
            if idx == "westcoast":
                idx_tz = timezone('America/Los_Angeles')
            if idx == "midwest":
                idx_tz = timezone('America/Chicago')
            if idx == "eastcoast":
                idx_tz = timezone('America/New_York')
        
            idx_dt = arg_dt.astimezone(idx_tz)
            current_time = idx_dt.strftime(FMT)
            temp_output = pd.DataFrame([[idx, current_time]], columns=['region', 'current time'])
            print(temp_output)
            #self.data = self.data.append(temp_output)

    def run(self, arg):
        """
        Put it all together into a single function call that returns 
        a dataframe with your results
        """
        self.region(arg)
        self.time_diff(arg)
        #print(self.data)

# demo 
#inst = timezones()
#inst.run("westcoast")


