# analysis.py
# Program to read in Fisher's Iris dataset, perfom exploratory data anaysis, 
# and plot features of the data.

# Author: Susan Collins

# Library to allow file-handling
import sys

# variable to hold Iris data filename
FILENAME = "iris.data"

with open (FILENAME, 'rt') as iris:

    # Sanity check - read in and print out iris data
        print(iris.read())