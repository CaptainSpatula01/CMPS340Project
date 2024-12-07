# Version: v0.2
# Date Last Updated: 12-06-2024
#%% STANDARDS - DO NOT include this block in a new module


#%% MODULE BEGINS
module_name = 'parent_child_classes'
'''
Version: v0.2
Description:
Extends Person (Parent) and Employee (Child) classes with data visualization, advanced querying, 
and configuration constants.
Authors:
Bryce Norris, Fiyinfoluwa Osifala, Davidson Rock
Date Created: 11-20-2024
Date Last Updated: 12-06-2024
Doc:
This module includes data visualization, querying functionalities, and 
advanced configuration handling for Person and Employee classes.
'''

#%% IMPORTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from copy import deepcopy as dpcpy
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from config import CONFIG  # Importing the config file

#%% USER INTERFACE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# No user interface components for this module.

#%% DECLARATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Person:
    '''
    Parent class to represent a Person with basic attributes.
    '''

    def __init__(self, fname, lname, dob):
        '''
        Initialize a Person object.
        '''
        self.first_name = fname
        self.last_name = lname
        self.date_of_birth = dt.datetime.strptime(dob, CONFIG["DATE_FORMAT"]).date()

    def to_dict(self):
        '''
        Convert Person object attributes to a dictionary.
        '''
        return {
            "First Name": self.first_name,
            "Last Name": self.last_name,
            "Date of Birth": self.date_of_birth.strftime(CONFIG["DATE_FORMAT"])
        }

    @staticmethod
    def read_file():
        '''
        Read the CSV file and return a list of Person objects.
        '''
        data = pd.read_csv(CONFIG["FILE_PATH"])
        people = [Person(row['First Name'], row['Last Name'], row['Date of Birth']) for _, row in data.iterrows()]
        return people

    @staticmethod
    def query_by_year(year):
        '''
        Query people born after a specific year.
        '''
        data = pd.read_csv(CONFIG["FILE_PATH"])
        filtered_data = data[pd.to_datetime(data['Date of Birth']).dt.year > year]
        return filtered_data

    def __str__(self):
        '''
        String representation of a Person object.
        '''
        return f"{self.first_name} {self.last_name}, DOB: {self.date_of_birth}"

    @staticmethod
    def plot_histogram(column):
        '''
        Plot a histogram for a specific column.
        '''
        data = pd.read_csv(CONFIG["FILE_PATH"])
        data[column].hist()
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.show()

    @staticmethod
    def plot_line(column):
        '''
        Plot a line chart for a specific column.
        '''
        data = pd.read_csv(CONFIG["FILE_PATH"])
        plt.plot(data[column])
        plt.title(f"Line Plot of {column}")
        plt.xlabel("Index")
        plt.ylabel(column)
        plt.show()


class Employee(Person):
    '''
    Child class inheriting from Person with additional functionalities.
    '''

    def __init__(self, fname, lname, dob):
        '''
        Initialize an Employee object.
        '''
        super().__init__(fname, lname, dob)

    @staticmethod
    def read_file():
        '''
        Read the CSV file and return a list of Employee objects.
        '''
        data = pd.read_csv(CONFIG["FILE_PATH"])
        employees = [
            Employee(
                row['First Name'],
                row['Last Name'],
                row['Date of Birth']
            )
            for _, row in data.iterrows()
        ]
        return employees

    @staticmethod
    def plot_violin(column):
        '''
        Plot a violin plot for a specific column.
        '''
        data = pd.read_csv(CONFIG["FILE_PATH"])
        sns.violinplot(x=data[column])
        plt.title(f"Violin Plot of {column}")
        plt.show()

    @staticmethod
    def plot_box(column):
        '''
        Plot a box plot for a specific column.
        '''
        data = pd.read_csv(CONFIG["FILE_PATH"])
        sns.boxplot(x=data[column])
        plt.title(f"Box Plot of {column}")
        plt.show()

    @staticmethod
    def plot_scatter(x_col, y_col):
        '''
        Plot a scatter plot between two columns.
        '''
        data = pd.read_csv(CONFIG["FILE_PATH"])
        plt.scatter(data[x_col], data[y_col])
        plt.title(f"Scatter Plot: {x_col} vs {y_col}")
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.show()

    def __str__(self):
        '''
        String representation of an Employee object.
        '''
        return super().__str__()


# Function definitions Start Here
def main():
    '''
    Main function to test Person and Employee classes.
    '''
    # Test Person class
    print("List of People:")
    people = Person.read_file()
    for person in people:
        print(person.to_dict())

    # Test Employee class
    print("\nList of Employees:")
    employees = Employee.read_file()
    for employee in employees:
        print(employee.to_dict())

    # Test Visualizations
    print("\nVisualizing data:")
    Person.plot_histogram('Age')  # Replace 'First Name' with a numeric column
    Employee.plot_violin('Salary')  # Replace 'First Name' with a numeric column


#%% MAIN CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main code starts here
# Testing is contained in the main function.

#%% SELF-RUN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main Self-run block
if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")
    main()
