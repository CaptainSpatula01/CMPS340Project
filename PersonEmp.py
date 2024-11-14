# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:14:04 2024

@authors: Davidson Rock, Fiyinfoluwa Osifala, Bryce Norris
"""

'''
Unless otherwise required, use the following guidelines
* Style:
    - Write the code in aesthetically-pleasing style
    - Names should be self-explanatory
    - Comment adequately.
    - Use relative path
    - Use generic coding instead of manually-entered constant values
    - Legends should be good enough in color, linestyle, shape etc. to distinguish data series.
    - Always test your code with an artificial data whose return value is known.
    - Sort imports alphabetically.
 
* Performance and Safety:
    - Avoid global variables; if needed, add suffix "_gl".
    - Code must be efficient.
    - Avoid if-blocks, declarations, and initializations in loops unless required.
    - Save data in categorized folders.
    - import only needed components from packages/modules.

'''

#%% MODULE BEGINS
module_name = '<PersonEmp>'

'''
Version: <0.2>

Description:
    Basic person and employee classes with data input format and functionality to read data from a file.

Authors:
    Davidson Rock, Fiyinfoluwa Osifala, Bryce Norris

Date Created     :  November 12th, 2024
Date Last Updated:  November 13th, 2024

Doc:
    <***>

Notes:
    <***>
'''

#%% IMPORTS                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from copy import deepcopy as dpcpy
import pandas as pd
import datetime

#%% DATA INPUT SPECIFICATION    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Expected input format for person data in CSV format:
# Columns:
# - First Name (str): The first name of the person.
# - Last Name (str): The last name of the person.
# - Date of Birth (str in YYYY-MM-DD format): The date of birth of the person.
# - Job (str, optional): The job title of the person, applicable for Employee objects.



#%% CLASS DEFINITIONS          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Person:
    def __init__(self, fname, lname, dob):
        self.first_name = fname
        self.last_name = lname
        self.date_of_birth = datetime.datetime.strptime(dob, "%Y-%m-%d").date()


class Employee(Person):
    def __init__(self, fname, lname, dob, job):
        super().__init__(fname, lname, dob)
        self.job = job

    @staticmethod
    def read_file(file_path):
        """
        Reads a CSV file and returns a list of Employee objects.

        Parameters:
            file_path (str): The path to the CSV file containing employee data.

        Returns:
            employees (list): A list of Employee instances.
        """
        data = pd.read_csv(file_path)
        employees = []

        for _, row in data.iterrows():
            employee = Employee(
                fname=row['First Name'],
                lname=row['Last Name'],
                dob=row['Date of Birth'],
                job=row['Job'] if 'Job' in row else None
            )
            employees.append(employee)

        return employees

#%% FUNCTION DEFINITIONS       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():
    # Example usage of read_file function
    file_path = './data/person_data.csv'  
    employees = Employee.read_file(file_path)
    for emp in employees:
        print(emp.to_dict())


#%% MAIN CODE                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")
    main()
