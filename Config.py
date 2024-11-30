#Version: v0.2
#Date Last Updated: 11-30-2024
#%% STANDARDS - DO NOT include this block in a new module

#%% MODULE BEGINS
module_name = 'Config'

"""
Version: v0.2
Description:
Contains configuration constants and shared settings for the Person-Employee system.
Authors:
Bryce Norris, Fiyinfoluwa Osifala, Davidson Rock
Date Created: 11-20-2024
Date Last Updated: 11-30-2024
Doc:
Provides centralized settings such as file paths, date formats, and others.
Notes:
Ensure this file is imported wherever configuration values are needed.
"""

#%% IMPORTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import logging

#%% USER INTERFACE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#%% CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DATE_FORMAT = "%Y-%m-%d"  # Define date format constant
FILE_PATH = "your_file.csv"  # Define the file path for the CSV file

#%% CONFIGURATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

#%% INITIALIZATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#%% DECLARATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function definitions Start Here
def get_file_path():
    """
    Get the file path for the data file.
    Includes error handling.
    """
    try:
        return FILE_PATH
    except Exception as e:
        logging.error(f"Error retrieving file path: {e}")
        return None

def get_date_format():
    """
    Get the standard date format.
    Includes error handling.
    """
    try:
        return DATE_FORMAT
    except Exception as e:
        logging.error(f"Error retrieving date format: {e}")
        return None

#%% MAIN CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#%% SELF-RUN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")
    print(f"File Path: {get_file_path()}")
    print(f"Date Format: {get_date_format()}")
