#!/usr/bin/env python
from __future__ import print_function

import os
import sys

import igc_lib
import lib.dumpers as dumpers
from datetime import date

def print_flight_details(flight):
    for i in range(len(flight.exits)):
        print(date.fromtimestamp(flight.date_timestamp).strftime("%d/%m/%y"), ",", flight.pilot_name,",", flight.glider_type, ",", flight.exits[i])


def main():
    if len(sys.argv) < 2:
        print("Usage: %s file.igc [file.lkt]" % sys.argv[0])
        sys.exit(1)

    input_file = sys.argv[1]
    task_file = None
    if len(sys.argv) > 2:
        task_file = sys.argv[2]

    flight = igc_lib.Flight.create_from_file(input_file)
    if not flight.valid:
        print("Provided flight is invalid:")
        print(flight.notes)
        sys.exit(1)

    print_flight_details(flight)

    if task_file:
        task = igc_lib.Task.create_from_lkt_file(task_file)
        reached_turnpoints = task.check_flight(flight)
        for t, fix in enumerate(reached_turnpoints):
            print("Turnpoint[%d] achieved at:" % t, fix.rawtime)


if __name__ == "__main__":
    main()
