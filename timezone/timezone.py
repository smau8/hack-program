#!/usr/bin/env python

"""
A function for displaying different timezones within the US. 
"""

import datetime


def region(arg):
    """
    returns the timezone information
    """

    # print days til Darwin's birthday
    if arg == "westcoast":
        print("3 hours behind east coast")
        print("2 hours behind midwest")

    elif arg == "midwest":
        print("1 hour behind east coast")
        print("2 hours ahead west coast")
    
    elif arg == "eastcoast":
        print("3 hours ahead west coast")
        print("1 hour ahead midwest") 



if __name__ == "__main__":
    region('westcoast')
    region('eastcoast')
    region('midwest')
