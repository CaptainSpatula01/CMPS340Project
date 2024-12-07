#Version: v0.2
#Date Last Updated: 12-06-2024

#%% MODULE BEGINS
module_name = 'main'
'''
Version: v0.2
Description:
Entry point for testing the Person-Employee and Product-ElectronicDevice systems. Integrates visualization and configuration settings.
Authors:
Bryce Norris , Fiyinfoluwa Osifala , Davidson Rock
Date Created: 11-20-2024
Date Last Updated: 12-06-2024
Doc:
Tests the functionality of all classes and visualization functions.
'''

#%% IMPORTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import Config
from person_employee import Person, Employee
from Product_ElectronicDevice import Product, ElectronicDevice
from visualizations import plot_violin, plot_box, plot_histogram, plot_scatter
import pandas as pd

#%% CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FILE_PATH = Config.get_file_path()
DATE_FORMAT = Config.get_date_format()

#%% FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def read_and_display(file_read_function, description):
    '''
    Generic function to read and display data using the provided file reading function.
    '''
    print(f"\n{description}:")
    try:
        items = file_read_function()
        for item in items:
            print(item.to_dict())
        return items
    except Exception as e:
        print(f"Error reading {description}: {e}")
        return None

def test_visualizations(data):
    '''
    Test visualization functions using sample data.
    '''
    print("\nTesting Visualizations...")
    try:
        if data is not None:
            plot_histogram(data, "Age")  # Example histogram
            plot_violin(data, "Age")    # Example violin plot
            plot_box(data, "Salary")    # Example box plot
            plot_scatter(data, "Age", "Salary")  # Example scatter plot
        else:
            print("Visualization tests skipped (no data).")
    except Exception as e:
        print(f"Error during visualization tests: {e}")

#%% MAIN FUNCTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    '''
    Main function to test classes and visualizations.
    '''
    print(f"Using File Path: {FILE_PATH}")
    print(f"Using Date Format: {DATE_FORMAT}")

    # Test Person and Employee classes
    people = read_and_display(Person.read_file, "List of People")
    employees = read_and_display(Employee.read_file, "List of Employees")

    # Test Product and ElectronicDevice classes
    products = read_and_display(Product.read_file, "List of Products")
    devices = read_and_display(ElectronicDevice.read_file, "List of Electronic Devices")

    # Visualization tests
    test_visualizations(pd.read_csv(FILE_PATH))

#%% SELF-RUN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")
    main()
