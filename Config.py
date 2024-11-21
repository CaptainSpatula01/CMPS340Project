#Version: v0.1
#Date Last Updated: 11-20-2024
#%% STANDARDS - DO NOT include this block in a new module
'''
Refer to the provided standards for code style, performance, and safety.
'''

#%% MODULE BEGINS
module_name = 'config'
'''
Version: v0.1
Description:
Contains configuration constants and shared settings for the Person-Employee system.
Authors:
Bryce Norris , Fiyinfoluwa Osifala , Davidson Rock
Date Created: 11-20-2024
Date Last Updated: 11-20-2024
Doc:
Provides centralized settings such as file paths, date formats, and others.
Notes:
Ensure this file is imported wherever configuration values are needed.
'''

#%% IMPORTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# None required for this configuration module.

#%% USER INTERFACE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#%% CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DATE_FORMAT = "%Y-%m-%d"  # Define date format constant
FILE_PATH = "your_file.csv"  # Define the file path for the CSV file

#%% CONFIGURATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# No additional configurations at the moment.

#%% INITIALIZATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#%% DECLARATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function definitions Start Here
def get_file_path():
    '''
    Get the file path for the data file.
    '''
    return FILE_PATH

def get_date_format():
    '''
    Get the standard date format.
    '''
    return DATE_FORMAT

#%% MAIN CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#%% SELF-RUN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")
    print(f"File Path: {FILE_PATH}")
    print(f"Date Format: {DATE_FORMAT}")
