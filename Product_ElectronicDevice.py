#Version: v0.3
#Date Last Updated: 12-06-2024
#%% MODULE BEGINS
module_name = 'Product_ElectronicDevice'
'''
Version: v0.3
Description:
Defines Product (Parent) and ElectronicDevice (Child) classes with basic attributes and file integration, and integrates visualization functions from visualizations.py.
Authors:
Bryce Norris , Fiyinfoluwa Osifala , Davidson Rock
Date Created: 11-30-2024
Date Last Updated: 12-06-2024
Doc:
This module contains two classes, Product and ElectronicDevice, and their associated
methods for CSV file handling and data manipulation.
'''


#%% IMPORTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import numpy as np
from copy import deepcopy as dpcpy
import datetime as dt
import pandas as pd
import os
from visualizations import plot_price_histogram, plot_scatter_manufactured_date  # Import visualization functions

#%% CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DATE_FORMAT = "%Y-%m-%d"  # Define date format constant
__FILE_PATH = "product_file.csv"  # Define the file to be read

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
        return np.dot(vec1, vec2) == 0


class ElectronicDevice(Product):
    '''
    Child class inheriting from Product, representing electronic devices.
    '''

    def __init__(self, name, price, manufactured_date):
        '''
        Initialize an ElectronicDevice object.
        '''
        super().__init__(name, price, manufactured_date)

#%% MAIN CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main code starts here for testing. Can be moved to a separate script for testing.

if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")
    
    # Test Product class
    try:
        products = Product.read_file()
        for product in products:
            print(product.to_dict())
    except Exception as e:
        print(f"Error reading Products: {e}")

    # Test Visualization
    try:
        product_data = pd.read_csv(FILE_PATH)
        product = Product('', 0, '')  # Creating a dummy Product to use its methods
        plot_price_histogram(product_data)  # Call the imported visualization function
        plot_scatter_manufactured_date(product_data)  # Call the imported visualization function
    except Exception as e:
        print(f"Error during visualization tests: {e}")

    # Test Statistical Methods
    print(f"Mean Price: ${Product.mean_price():.2f}")
    print(f"Median Price: ${Product.median_price():.2f}")
    print(f"Standard Deviation of Price: ${Product.std_price():.2f}")

    # Test Vector Operations
    vec1 = [1, 2, 3]
    vec2 = [4, 5, 6]
    print(f"Dot Product: {Product.dot_product(vec1, vec2)}")
    print(f"Angle Between Vectors: {Product.angle_between_vectors(vec1, vec2)} radians")
    print(f"Are vectors orthogonal? {'Yes' if Product.check_orthogonality(vec1, vec2) else 'No'}")
