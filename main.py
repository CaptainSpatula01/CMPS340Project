#Version: v0.1
#Date Last Updated: 11-30-2024
#%% STANDARDS - DO NOT include this block in a new module
'''
Refer to the provided standards for code style, performance, and safety.
'''

#%% MODULE BEGINS
module_name = 'main'
'''
Version: v0.1
Description:
Entry point for testing the Person-Employee system. It integrates configuration and class modules.
Authors:
Bryce Norris , Fiyinfoluwa Osifala , Davidson Rock
Date Created: 11-20-2024
Date Last Updated: 11-30-2024
Doc:
Tests the functionality of Person and Employee classes and verifies the integration with config settings.
Notes:
Ensure the `your_file.csv` file exists in the project directory.
'''

#%% IMPORTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import config
from parent_child_classes import Person, Employee

#%% USER INTERFACE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#%% CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FILE_PATH = config.get_file_path()
DATE_FORMAT = config.get_date_format()

#%% CONFIGURATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#%% INITIALIZATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#%% DECLARATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    '''
    Main function to test Person and Employee classes using configuration.
    '''
    print(f"Using File Path: {FILE_PATH}")
    print(f"Using Date Format: {DATE_FORMAT}")

     # Test Person class
    print("\nList of People:")
    try:
        people = Person.read_file()
        for person in people:
            print(person.to_dict())
    except Exception as e:
        print(f"Error reading People: {e}")

    # Test Employee class
    print("\nList of Employees:")
    try:
        employees = Employee.read_file()
        for employee in employees:
            print(employee.to_dict())
    except Exception as e:
        print(f"Error reading Employees: {e}")

    # Test Product class
    print("\nList of Products:")
    try:
        products = Product.read_file()
        for product in products:
            print(product.to_dict())
    except Exception as e:
        print(f"Error reading Products: {e}")

    # Test ElectronicDevice class
    print("\nList of Electronic Devices:")
    try:
        devices = ElectronicDevice.read_file()
        for device in devices:
            print(device.to_dict())
    except Exception as e:
        print(f"Error reading Electronic Devices: {e}")

#%% MAIN CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#%% SELF-RUN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")
    main()
