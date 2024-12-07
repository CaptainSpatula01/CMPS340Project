# Version: v0.4
# Date Last Updated: 12-07-2024

#%% MODULE BEGINS
module_name = 'Product_ElectronicDevice'
'''
Version: v0.4
Description:
Defines Product (Parent) and ElectronicDevice (Child) classes with basic attributes and file integration, and integrates visualization functions from visualizations.py.
Authors:
Bryce Norris , Fiyinfoluwa Osifala , Davidson Rock
Date Created: 11-30-2024
Date Last Updated: 12-07-2024
Doc:
This module contains two classes, Product and ElectronicDevice, and their associated
methods for CSV file handling, data manipulation, and advanced operations.
'''

#%% IMPORTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import numpy as np
from copy import deepcopy as dpcpy
import datetime as dt
import pandas as pd
import os
import pickle
from itertools import permutations, combinations
from visualizations import plot_price_histogram, plot_scatter_manufactured_date

#%% CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DATE_FORMAT = "%Y-%m-%d"  # Define date format constant
FILE_PATH = "product_file.csv"  # Define the file to be read

#%% CLASS DEFINITIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Product:
    '''
    Parent class to represent a Product with basic attributes.
    '''

    def __init__(self, name, price, manufactured_date):
        '''
        Initialize a Product object.
        '''
        self.name = name
        self.price = float(price)
        try:
            self.manufactured_date = dt.datetime.strptime(manufactured_date, DATE_FORMAT).date()
        except ValueError:
            self.manufactured_date = None  # Set to None if the date is invalid

    def to_dict(self):
        '''
        Convert Product object attributes to a dictionary.
        '''
        return {
            "Name": self.name,
            "Price": self.price,
            "Manufactured Date": self.manufactured_date.strftime(DATE_FORMAT) if self.manufactured_date else 'N/A'
        }

    @classmethod
    def read_file(cls, file_path=None, **kwargs):
        '''
        Read the CSV file and return a list of Product objects.
        '''
        file_path = file_path or FILE_PATH  # Use provided file path or default one
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        try:
            data = pd.read_csv(file_path)
            if not all(col in data.columns for col in ['Name', 'Price', 'Manufactured Date']):
                raise ValueError("CSV file is missing required columns.")
            return [cls(row['Name'], row['Price'], row['Manufactured Date']) for _, row in data.iterrows()]
        except pd.errors.EmptyDataError:
            raise ValueError(f"File {file_path} is empty.")

    def __str__(self):
        '''
        String representation of a Product object.
        '''
        return f"{self.name} - ${self.price:.2f}, Manufactured: {self.manufactured_date if self.manufactured_date else 'N/A'}"

    @classmethod
    def filter_by_price(cls, min_price, max_price):
        '''
        Filter products by price range.
        '''
        data = pd.read_csv(FILE_PATH)
        filtered_data = data[(data['Price'] >= min_price) & (data['Price'] <= max_price)]
        return [cls(row['Name'], row['Price'], row['Manufactured Date']) for _, row in filtered_data.iterrows()]

    @classmethod
    def mean_price(cls):
        '''
        Calculate the mean price of all products.
        '''
        data = pd.read_csv(FILE_PATH)
        return data['Price'].mean()

    @classmethod
    def median_price(cls):
        '''
        Calculate the median price of all products.
        '''
        data = pd.read_csv(FILE_PATH)
        return data['Price'].median()

    @classmethod
    def std_price(cls):
        '''
        Calculate the standard deviation of product prices.
        '''
        data = pd.read_csv(FILE_PATH)
        return data['Price'].std()

    @staticmethod
    def dot_product(vec1, vec2):
        '''
        Calculate dot product of two vectors.
        '''
        return np.dot(vec1, vec2)

    @staticmethod
    def angle_between_vectors(vec1, vec2):
        '''
        Calculate the angle between two vectors.
        '''
        dot_product = np.dot(vec1, vec2)
        norm_vec1 = np.linalg.norm(vec1)
        norm_vec2 = np.linalg.norm(vec2)
        return np.arccos(dot_product / (norm_vec1 * norm_vec2))

    @staticmethod
    def check_orthogonality(vec1, vec2):
        '''
        Check if two vectors are orthogonal.
        '''
        return np.isclose(np.dot(vec1, vec2), 0)


class ElectronicDevice(Product):
    '''
    Child class inheriting from Product, representing electronic devices.
    Includes additional functionality for data manipulation, probability calculations,
    vector operations, and categorical attribute analysis.
    '''

    def __init__(self, name, price, manufactured_date):
        '''
        Initialize an ElectronicDevice object.
        '''
        super().__init__(name, price, manufactured_date)

    @classmethod
    def read_pickle_file(cls, file_path):
        '''
        Read data from a pickle file and return a list of ElectronicDevice objects.
        '''
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Pickle file not found: {file_path}")
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        return [cls(**item) for item in data]

    @staticmethod
    def calculate_probabilities(data, attr1, attr2=None):
        '''
        Calculate and display joint counts, joint probabilities, and conditional probabilities.
        '''
        if attr2:
            joint_counts = pd.crosstab(data[attr1], data[attr2])
            joint_probabilities = joint_counts / joint_counts.sum().sum()
            conditional_probabilities = joint_counts.div(joint_counts.sum(axis=1), axis=0)
            return joint_counts, joint_probabilities, conditional_probabilities
        else:
            value_counts = data[attr1].value_counts()
            probabilities = value_counts / value_counts.sum()
            return value_counts, probabilities

    @staticmethod
    def calculate_statistics(data, numeric_attr):
        '''
        Calculate mean, median, and standard deviation for a numeric attribute.
        '''
        mean = data[numeric_attr].mean()
        median = data[numeric_attr].median()
        std = data[numeric_attr].std()
        return mean, median, std

    @staticmethod
    def vector_operations(vec1, vec2):
        '''
        Perform various vector operations:
        - Position vector
        - Unit vector
        - Projection vector
        - Dot product
        - Angle between vectors
        - Orthogonality check
        '''
        position_vector = np.array(vec1)
        unit_vector = position_vector / np.linalg.norm(position_vector)
        projection_vector = np.dot(position_vector, vec2) / np.linalg.norm(vec2)**2 * np.array(vec2)
        dot_product = np.dot(position_vector, vec2)
        angle = np.arccos(dot_product / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))
        is_orthogonal = np.isclose(dot_product, 0)
        return {
            "Position Vector": position_vector,
            "Unit Vector": unit_vector,
            "Projection Vector": projection_vector,
            "Dot Product": dot_product,
            "Angle (radians)": angle,
            "Orthogonal": is_orthogonal
        }

    @staticmethod
    def categorical_analysis(data, categorical_attr):
        '''
        Perform operations on a categorical attribute:
        - Obtain unique values
        - Generate permutations
        - Generate combinations
        '''
        unique_values = data[categorical_attr].unique()
        perms = list(permutations(unique_values, 2))
        combs = list(combinations(unique_values, 2))
        return unique_values, perms, combs

    @staticmethod
    def export_data(data, file_name):
        '''
        Export data (e.g., probabilities, vectors) to a CSV file.
        '''
        df = pd.DataFrame(data)
        df.to_csv(file_name, index=False)
        print(f"Data exported successfully to {file_name}")
