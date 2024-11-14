# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:14:04 2024

@author: Davidson Rock, Fiyinfoluwa Osifala, Bryce Norris
"""

'''
Unless otherwise required, use the following guidelines:
* Style, Performance, and Safety (see full standards in module_tmp.py)
'''

#%% MODULE BEGINS
module_name = '<Person>'

'''
Version: <0.1>

Description:
    <Basic person class and employee subclass with data handling functionality>

Authors:
    Davidson Rock, Fiyinfoluwa Osifala, Bryce Norris

Date Created     :  November 12th, 2024
Date Last Updated:  November 13th, 2024
'''

#%% IMPORTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from copy import deepcopy as dpcpy
from datetime import date
import pandas as pd
import os

#%% CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DEFAULT_CSV_PATH = os.path.join("data", "persons_data.csv")

#%% CLASS DEFINITIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Person:
    """A class to represent a person with basic attributes."""

    def __init__(self, fname: str, lname: str, dob: date):
        """
        Initializes a new person instance.

        Args:
            fname (str): First name of the person.
            lname (str): Last name of the person.
            dob (date): Date of birth of the person.
        """
        self.first_name = fname
        self.last_name = lname
        self.date_of_birth = dob  # Set date of birth with type date.

    def to_dict(self) -> dict:
        """
        Returns the person's data in dictionary format.
        
        Returns:
            dict: A dictionary containing the person's details.
        """
        return {
            "First Name": self.first_name,
            "Last Name": self.last_name,
            "Date of Birth": self.date_of_birth
        }


class Employee(Person):
    """A subclass of Person to represent an employee with job details."""

    def __init__(self, fname: str, lname: str, dob: date, job: str, employee_id: int):
        """
        Initializes a new employee instance.

        Args:
            fname (str): First name of the employee.
            lname (str): Last name of the employee.
            dob (date): Date of birth of the employee.
            job (str): Job title of the employee.
            employee_id (int): Unique ID of the employee.
        """
        super().__init__(fname, lname, dob)
        self.job = job
        self.employee_id = employee_id

    @staticmethod
    def read_file(file_path: str = DEFAULT_CSV_PATH) -> pd.DataFrame:
        """
        Reads input file (CSV) and stores data in a DataFrame.

        Args:
            file_path (str): Path to the CSV file. Defaults to DEFAULT_CSV_PATH.

        Returns:
            pd.DataFrame: A DataFrame containing the file's data.
        """
        try:
            data_df = pd.read_csv(file_path)
            print("Data loaded successfully from CSV.")
            return data_df
        except FileNotFoundError:
            print(f"File not found at path: {file_path}")
            return pd.DataFrame()

#%% FUNCTION DEFINITIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def plot_dob(data_df: pd.DataFrame):
    """
    Plots the date of birth distribution for all persons in the DataFrame.

    Args:
        data_df (pd.DataFrame): DataFrame containing person data.
    """
    if 'Date of Birth' not in data_df.columns:
        print("Error: Date of Birth column not found in DataFrame.")
        return
    
    # Convert to datetime if not already
    data_df['Date of Birth'] = pd.to_datetime(data_df['Date of Birth'], errors='coerce')
    
    # Plot the histogram
    data_df['Date of Birth'].dt.year.plot(kind='hist', title="Birth Year Distribution")
    plt.xlabel("Year of Birth")
    plt.ylabel("Frequency")
    plt.show()

def main():
    # Example usage:
    sample_employee = Employee("Alice", "Smith", date(1990, 5, 21), "Engineer", 101)
    print(sample_employee.to_dict())

    # Load and plot data from CSV
    df_persons = Employee.read_file()
    if not df_persons.empty:
        plot_dob(df_persons)

#%% SELF-RUN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")
    main()
