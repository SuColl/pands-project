# analysis.py
# Program to read in Fisher's Iris dataset, perfom exploratory data anaysis, 
# and plot features of the data.

# Author: Susan Collins

# Library to allow file-handling
import sys
# Library for data analysis
import pandas as pd
# Libraries for plotting
import matplotlib.pyplot as plt
import seaborn as sns

# variable to hold Iris data filename
INPUT_FILENAME = "bezdekiris.data"

# variable to hold filename of text file to contain a summary of each feature
OUTPUT_FILENAME = "iris_stats.txt"

# List of features (columns) in the data
feature_names = ["sepal length", "sepal width", "petal length", "petal width"]

# open data file and read into dataframe
with open (INPUT_FILENAME, 'rt') as iris_file:

    # Create Pandas DataFrame from the iris data file.
    # Add column names manually as they are not present in the iris.data file.
    iris = pd.read_csv(
        iris_file, 
        names=feature_names + ["species"]
        )
    

# print out dataframe statistics per feature, overwrite file if exists
with open (OUTPUT_FILENAME, 'w+t') as stats_file:
    print(iris.describe(), file=stats_file)


# Use Pyplot to create multiplot histogram of each feature in iris data
fig, ax = plt.subplots(2, 2, layout ='constrained', figsize=(8, 6)) 
# Create variable to iterate over the subplots
this_subplot = 0

# For each feature, by name
for index, feature in enumerate(feature_names):

    # set which subplot we are working on, counting from 1   
    plt.subplot(2, 2, index+1)
    
    # set number of bins 
    nbins = 25

    # Only plot the legend on the last subplot
    if index == 3:
        plot_legend_flag = True
    else:
        plot_legend_flag = False

    # Use Seaborn to plot histograms
    # ref: https://seaborn.pydata.org/generated/seaborn.histplot.html
    # As data for all targets is called in one plot command, the histogram
    # bins are the same across all three targets
    sns.histplot(
        iris, 
        x=feature,
        bins=nbins,
        hue='species',
        hue_order=["Iris-setosa","Iris-versicolor","Iris-virginica"],
        alpha=0.5,
        edgecolor='black',
        legend=plot_legend_flag
        )

    # Set the x-axis label to the feature name, plus units
    plt.xlabel(feature + " (cm)")

    # Set the y-axis label to frequency in the dataset
    plt.ylabel("Frequency")

# Set overall title
fig.suptitle("Histograms of features in the Iris Dataset")

# Print to file
plt.savefig('plot01_histograms_of_iris_features.png')