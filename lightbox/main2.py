# -*- coding: utf-8 -*-

"""Main module."""
import sys
import click
import urllib.request
import argparse 
import requests 
from urllib.request import urlopen
import os
import re

click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """Console script for led_tester."""
    print("input", input)

    N, instructions = parseFile(input)

    ledTester = LEDTester(N)

    for instruction in instructions:
        ledTester.apply(instruction)

    print('#occupied: ', ledTester.countOccupied()) 
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover