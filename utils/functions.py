import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



def pairplotter(df, hue=None, size=2.5, palette='#A4064D', corner=True):
    """
    Function to plot pairplot for the DataFrame.
    
    Parameters:
    df (DataFrame): The DataFrame to plot.
    hue (str): Column name to color the points by.
    size (float): Size of the plot.
    palette (str): Color palette for the plot.
    corner (bool): If True, only plot the lower triangle of the pairplot.
    """
    sns.pairplot(df, hue=hue, corner=corner, plot_kws={'color': palette}, height=size)
    plt.show()

def boxplotter_all(df, hue=None, palette='#A4064D', corner=True, figsize=(6, 6), size=0.5):
    """
    Function to plot boxplot for the DataFrame.
    
    Parameters:
    df (DataFrame): The DataFrame to plot.
    hue (str): Column name to color the boxes by.
    palette (str): Color palette for the plot.
    """
    
    for col in df:
        plt.figure(figsize=(12, 6))
        sns.boxplot(y=col, data=df, hue=hue, palette=palette)
        plt.xticks(rotation=45)
        plt.show()

def remove_outliers_iqr(df, column):
    """
    Function to remove outliers from a DataFrame using the IQR method.
    
    Parameters:
    df (DataFrame): The DataFrame to process.
    column (str): The column name to remove outliers

    Returns:
    DataFrame: The DataFrame with outliers removed.
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

def remove_outliers_upper_quantile(df, column, quantile=0.90):

    """
    Function to remove outliers from a DataFrame using the upper quantile method.
    
    Parameters:
    df (DataFrame): The DataFrame to process.
    column (str): The column name to remove outliers
    quantile (float): The quantile to use for upper bound (default is 0.90)

    Returns:
    DataFrame: The DataFrame with outliers removed.
    """
    upper_bound = df[column].quantile(quantile)
    return df[df[column] <= upper_bound]

def countplotter(df, hue=None, palette='rocket'):
    """
    Function to plot countplot for a specific column in the DataFrame.
    
    Parameters:
    df (DataFrame): The DataFrame to plot.
    hue (str): Column name to color the bars by.
    palette (str): Color palette for the plot.
    """
    for col in df:
        plt.figure(figsize=(6, 3))
        sns.countplot(x=col, data=df, hue=hue, palette=palette)
        plt.xticks(rotation=45)
        plt.title(f'Countplot of {col}')
        plt.show()