# Version: v0.1
# Date Last Updated: 11-30-2024
# %% STANDARDS - DO NOT include this block in a new module

# %% MODULE BEGINS
module_name = 'second_Parent_child_classes'
'''
Version: v0.1
Description:
Defines Product (Parent) and ElectronicDevice (Child) classes with basic attributes and file integration.
Authors:
Bryce Norris , Fiyinfoluwa Osifala , Davidson Rock
Date Created: 11-30-2024
Date Last Updated: 11-30-2024
Doc:
This module contains two classes, Product and ElectronicDevice, and their associated
methods for CSV file handling and data manipulation.
Notes:
The module follows the provided standard template.
'''

# %% IMPORTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from copy import deepcopy as dpcpy
import datetime as dt
import pandas as pd
import os
import matplotlib.pyplot as plt

# %% USER INTERFACE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# No user interface components for this module.

# %% CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DATE_FORMAT = "%Y-%m-%d"  # Define date format constant
FILE_PATH = "product_file.csv"  # Define the file to be read

# %% CONFIGURATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Configuration settings are implemented as constants for reusability.

# %% INITIALIZATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Initialize reusable variables or data structures if needed.

# %% DECLARATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Global declarations Start Here
# Class definitions Start Here

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
        self.manufactured_date = dt.datetime.strptime(manufactured_date, DATE_FORMAT).date()

    def to_dict(self):
        '''
        Convert Product object attributes to a dictionary.
        '''
        return {
            "Name": self.name,
            "Price": self.price,
            "Manufactured Date": self.manufactured_date.strftime(DATE_FORMAT)
        }

    @classmethod
    def read_file(cls):
        '''
        Read the CSV file and return a list of Product objects.
        '''
        if not os.path.isfile(FILE_PATH):
            raise FileNotFoundError(f"File not found: {FILE_PATH}")
        try:
            data = pd.read_csv(FILE_PATH)
            if not all(col in data.columns for col in ['Name', 'Price', 'Manufactured Date']):
                raise ValueError("CSV file is missing required columns.")
            return [cls(row['Name'], row['Price'], row['Manufactured Date']) for _, row in data.iterrows()]
        except pd.errors.EmptyDataError:
            raise ValueError(f"File {FILE_PATH} is empty.")

    def __str__(self):
        '''
        String representation of a Product object.
        '''
        return f"{self.name} - ${self.price:.2f}, Manufactured: {self.manufactured_date}"

    @staticmethod
    def plot_price_distribution(products):
        '''
        Plot distribution of prices for a list of products.
        '''
        prices = [product.price for product in products]
        plt.hist(prices, bins=10, color='blue', edgecolor='black')
        plt.title('Price Distribution')
        plt.xlabel('Price')
        plt.ylabel('Frequency')
        plt.show()

class ElectronicDevice(Product):
    '''
    Child class inheriting from Product, representing electronic devices.
    '''

    def __init__(self, name, price, manufactured_date, warranty_period):
        '''
        Initialize an ElectronicDevice object.
        '''
        super().__init__(name, price, manufactured_date)
        self.warranty_period = int(warranty_period)  # Warranty in months

    def to_dict(self):
        '''
        Convert ElectronicDevice object attributes to a dictionary.
        '''
        base_dict = super().to_dict()
        base_dict["Warranty Period (months)"] = self.warranty_period
        return base_dict

    def __str__(self):
        '''
        String representation of an ElectronicDevice object.
        '''
        return f"{super().__str__()}, Warranty: {self.warranty_period} months"

    @staticmethod
    def plot_warranty_distribution(devices):
        '''
        Plot distribution of warranty periods for a list of electronic devices.
        '''
        warranties = [device.warranty_period for device in devices]
        plt.hist(warranties, bins=10, color='green', edgecolor='black')
        plt.title('Warranty Period Distribution')
        plt.xlabel('Warranty Period (months)')
        plt.ylabel('Frequency')
        plt.show()

# %% MAIN CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main code starts here
# Testing is contained in the main function.

# %% SELF-RUN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")



