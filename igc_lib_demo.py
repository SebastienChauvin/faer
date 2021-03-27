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

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    if len(sys.argv) < 2:
        eprint("Usage: %s file.igc [file.lkt]" % sys.argv[0])
        sys.exit(1)

    input_file = sys.argv[1]

    flight = igc_lib.Flight.create_from_file(input_file)
    if not flight.valid:
        eprint("Provided flight is invalid:")
        eprint(flight.notes)
        sys.exit(1)

    print_flight_details(flight)

if __name__ == "__main__":
    main()
