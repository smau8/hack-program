#!/usr/bin/env python

"""
Command line interface to timezone
"""

import argparse
from timezone import timezones


def parse_command_line():
    """
    parses args for the region function
    """
    # init parser and add arguments
    parser = argparse.ArgumentParser()

    # add long args
    parser.add_argument(
        "--westcoast",
        help="returns timezone differences relative to the west coast",
        action="store_true")

    # add long args
    parser.add_argument(
        "--midwest",
        help="returns timezone differences relative to the midwest",
        action="store_true")

    parser.add_argument(
        "--eastcoast",
        help="returns timezone differences relative to the east coast",
        action="store_true")

    # parse args
    args = parser.parse_args()

    # check that user only entered one action arg
    if sum([args.westcoast, args.midwest, args.eastcoast]) > 1:
        raise SystemExit(
            "only one region at a time.")
    return args


def run_program():
    """
    run main function on parsed args
    """
    # get arguments from command line as a dict-like object
    args = parse_command_line()

    # pass argument to call darwinday function
    if args.westcoast:
        timezones.region(timezones, "westcoast")
        timezones.time_diff(timezones,"westcoast")
    elif args.midwest:
        timezones.region(timezones,"midwest")
        timezones.time_diff(timezones, "midwest")
    elif args.eastcoast:
        timezones.region(timezones, "eastcoast")
        timezones.time_diff(timezones, "eastcoast")
