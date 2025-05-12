# pands-project
Assessed project for the Programming and Scripting module, part of the 
Higher Diploma in Data Analytics course at Atlantic Technological University, 
Ireland, Spring 2025 

Author: Susan Collins

## Description of this repository

This repository comprises files containing [Fisher's Iris data set](https://en.wikipedia.org/wiki/Iris_flower_data_set), a Python program that performs exploratory data analysis on the data set, and a Jupyter notebook that explains and provides references for the code in this program. 

These files have been produced as part of an assessment for the Programming and Scripting module, part of the Higher Diploma in Data Analytics, at Atlantic Technological University, Ireland, Spring 2025.

The brief for this project is listed here: [Project 2025.pdf](https://github.com/andrewbeattycourseware/pands-courseware/blob/main/labs/Project%202025.pdf)

## Files in this repository
[README.md](https://github.com/SuColl/pands-project/blob/main/README.md)  - this file

[.gitignore](https://github.com/SuColl/pands-project/blob/main/.gitignore) - a standard Git configuration file to prevent the upload of unnecessary files to the repository

[requirements.txt](https://github.com/SuColl/pands-project/blob/main/requirements.txt) - a list of Python libraries required to run the code in the Juypter notebook

[bezdekiris.data](https://github.com/SuColl/pands-project/blob/main/bezdekIris.data) - the Iris data set, downloaded from the [UC Irving Machine Learning Repository](https://archive.ics.uci.edu/dataset/53/iris). This is the version corrected after [Bezdek et. al. (1999)](https://doi.org/10.1109/91.771092).

[analysis.py](https://github.com/SuColl/pands-project/blob/main/analysis.py) - a Python program that reads in the Iris data file and produces a text file summarising the statistical characteristics of the data features, and several plots of the data features. 

[commentary.ipynb](https://github.com/SuColl/pands-project/blob/main/commentary.ipynb) - a Jupyter notebook which breaks down the code in analysis.py, providing explanations, comments and references.

Outputs of analysis.py:
- [iris_stats.txt]() - a text file
- [plot01_histograms_of_iris_features.png](https://github.com/SuColl/pands-project/blob/main/plot01_histograms_of_iris_features.png) - a multipart plot of the distribution of data points for each measurement of the iris flowers, separated by species
- [plot02_scatterplot_petal_length_vs_sepal_length.png](https://github.com/SuColl/pands-project/blob/main/plot02_scatterplot_petal_length_vs_sepal_length.png) - a scatter plot of iris petal length ve sepal length, with a linear fit displayed for each species' data points,
- [plot03_pairplot.png](https://github.com/SuColl/pands-project/blob/main/plot03_pairplot.png) - a 4x4 pairplot of each feature in the dataset.

## Expected output of analysis.py
```
       sepal length  sepal width  petal length  petal width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.057333      3.758000     1.199333
std        0.828066     0.435866      1.765298     0.762238
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000

```

![](plot01_histograms_of_iris_features.png)

![](plot02_scatterplot_petal_length_vs_sepal_length.png)

![](plot03_pairplot.png)


## Technologies used in the creation of this repository
- Python v3.12.7
- Git
- GitHub
- Jupyter
