# analysis.py
# Program to read in Fisher's Iris dataset, perfom exploratory data anaysis, 
# and plot features of the data.

# Author: Susan Collins

# Library to allow file-handling
import sys
# Library for data analysis
import pandas as pd

# variable to hold Iris data filename
FILENAME = "bezdekiris.data"

with open (FILENAME, 'rt') as iris_file:

    # Create Pandas DataFrame from the iris data file.
    # Add column names manually as they are not present in the iris.data file.
    iris = pd.read_csv(
        iris_file, 
        names=[
            "sepal_length", 
            "sepal_width", 
            "petal_length", 
            "petal_width", 
            "species"])
    
# print out dataframe
print(iris)