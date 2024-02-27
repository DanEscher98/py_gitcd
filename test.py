#!/usr/bin/python3

import os
import sys


def cd(path):
    try:
        os.chdir(path)
        print(f"Changed directory to {os.getcwd()}")
    except Exception as e:
        print(f"Failed to change directory: {e}")


# Usage
if len(sys.argv) > 1:
    cd(sys.argv[1])
else:
    print("Please provide a path as an argument.")
