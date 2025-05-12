# analysis.py
# Program to read in Fisher's Iris dataset, perform exploratory data analysis, 
# and plot features of the data.

# Author: Susan Collins


# If any of these modules are not installed, program ends. 
# Below code re-used from weekly task program es.py
try:
    # Library to allow system exit functions
    import sys
    # Library for data analysis
    import pandas as pd
    # Libraries for plotting
    import matplotlib.pyplot as plt
    import seaborn as sns
except ModuleNotFoundError:
    exit(
        "This program requires certain Python modules.\n"
        "Please check requirements.txt, install these modules and try again.\n"
        "Goodbye.")    

# variable to hold Iris data filename
INPUT_FILENAME = "bezdekIris.data"

# variable to hold filename of text file to contain a summary of each feature
OUTPUT_FILENAME = "iris_stats.txt"

# List of features (columns) in the data
feature_names = ["sepal length", "sepal width", "petal length", "petal width"]


# open data file and read into dataframe
# Below error-handling code re-used from weekly task program es.py
try:
    with open (INPUT_FILENAME, 'rt') as iris_file:

        # Create Pandas DataFrame from the iris data file.
        # Add column names manually as they are not present in the iris.data file.
        iris = pd.read_csv(
            iris_file, 
            names=feature_names + ["species"]
            )

# Exception if the file does not exist
except FileNotFoundError:
    sys.exit(f"Error! The file {INPUT_FILENAME} does not exist.")

# Exception if the user does not have permissions to open the file
except PermissionError:
    sys.exit(
        f"Error! You do not have permission to read the file {INPUT_FILENAME}"
        )

# Exception if the file is not a text file
except UnicodeDecodeError:
    sys.exit(f"Error! The file {INPUT_FILENAME} is not a text file.")



# print out dataframe statistics per feature, overwrite file if exists
try:
    with open (OUTPUT_FILENAME, 'w+t') as stats_file:
        print(iris.describe(), file=stats_file)
except PermissionError:
    print(
        "Error! You do not have permission to write to/overwrite the "
        f"file {OUTPUT_FILENAME}. This program will skip this step."
        )


# Use Pyplot to create multiplot histogram of each feature in iris data
fig, ax = plt.subplots(2, 2, layout ='constrained', figsize=(8, 6)) 

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

# Print to file and close this figure, so the next one can be made. 
# ref: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html
try: 
    plt.savefig('plot01_histograms_of_iris_features.png')
except PermissionError:
    print(
        "Error! You do not have permission to create the histogram plot file."
        )
plt.close()



# Plot a demonstration scatter plot of petal length vs sepal length, with a linear fit for each species.
sns.scatterplot(
    iris, 
    x="sepal length", 
    y="petal length",
    hue="species"
    )

# for each unique value in the species column, plot a linear fit
for species in iris.species.unique():
    sns.regplot(
        iris[iris.species==species], 
        scatter=False,
        x="sepal length", 
        y="petal length",
        )

# add the title
plt.title(
    "Scatter plot of iris petal length vs sepal length,\n"
    "with a linear fit for each iris species."
)

# Print to file and close the plot
try:
    plt.savefig('plot02_scatterplot_petal_length_vs_sepal_length.png')
except PermissionError:
    print(
        "Error! You do not have permission to create the scatter plot file."
        )    
plt.close()



# Create Seaborn Pairplot
sns.pairplot(
    iris,
    hue='species' 
    )

# Add plot title
plt.suptitle("Pairplot of Features in Iris Data Set", y=1.02, size='xx-large');

# Print to file and close the plot
try:
    plt.savefig('plot03_pairplot.png')
except PermissionError:
    print(
        "Error! You do not have permission to create the pairplot file."
        )
plt.close()


