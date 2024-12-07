#Version: v0.1
#Date Last Updated: 11-20-2024
#%% STANDARDS - DO NOT include this block in a new module


#%% MODULE BEGINS
module_name = 'person_employee'
'''
Version: v0.1
Description:
Defines Person (Parent) and Employee (Child) classes with basic attributes and file integration.
Authors:
Bryce Norris , Fiyinfoluwa Osifala , Davidson Rock
Date Created: 11-20-2024
Date Last Updated: 11-20-2024
Doc:
This module contains two classes, Person and Employee, and their associated
methods for CSV file handling and data manipulation.
Notes:
The module follows the provided standard template.
'''

#%% IMPORTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from copy import deepcopy as dpcpy
import datetime as dt
import pandas as pd

#%% USER INTERFACE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# No user interface components for this module.

#%% CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DATE_FORMAT = "%Y-%m-%d"  # Define date format constant
FILE_PATH = "your_file.csv"  # Define the file to be read

#%% CONFIGURATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Configuration settings are implemented as constants for reusability.

#%% INITIALIZATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Initialize reusable variables or data structures if needed.

#%% DECLARATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Global declarations Start Here
# Class definitions Start Here
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
        self.date_of_birth = dt.datetime.strptime(dob, DATE_FORMAT).date()

    def to_dict(self):
        '''
        Convert Person object attributes to a dictionary.
        '''
        return {
            "First Name": self.first_name,
            "Last Name": self.last_name,
            "Date of Birth": self.date_of_birth.strftime(DATE_FORMAT)
        }

    @staticmethod
    def read_file():
        '''
        Read the CSV file (your_file.csv) and return a list of Person objects.
        '''
        data = pd.read_csv(FILE_PATH)
        people = [Person(row['First Name'], row['Last Name'], row['Date of Birth']) for _, row in data.iterrows()]
        return people

    def __str__(self):
        '''
        String representation of a Person object.
        '''
        return f"{self.first_name} {self.last_name}, DOB: {self.date_of_birth}"


class Employee(Person):
    '''
    Child class inheriting from Person. No additional attributes added.
    '''

    def __init__(self, fname, lname, dob):
        '''
        Initialize an Employee object.
        '''
        super().__init__(fname, lname, dob)

    @staticmethod
    def read_file():
        '''
        Read the CSV file (your_file.csv) and return a list of Employee objects.
        '''
        data = pd.read_csv(FILE_PATH)
        employees = [
            Employee(
                row['First Name'],
                row['Last Name'],
                row['Date of Birth']
            )
            for _, row in data.iterrows()
        ]
        return employees

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

#%% MAIN CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main code starts here
# Testing is contained in the main function.

#%% SELF-RUN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main Self-run block
if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")
    main()
