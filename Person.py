# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:14:04 2024

@author: david
"""

'''
Unless otherwise required, use the following guidelines
* Style:
    - Write the code in aesthetically-pleasing style
    - Names should be self-explanatory
        - "the main variable designator_variable group name": "child_parent"
            - pm_single, not singlepm, dataDf_grpL_1 , not dataDf_grpL1; "_1" is safer for bugs.
    - Comment adequately.
        - Add a comment for each code block, such as a loop-block, that describe the functionality
    - Use relative path
    - Use generic coding instead of manually-entered constant values
    - Legends should be good enough in color, linestyle, shape etc. to distinguish data series.
    - Always test your code with an artificial data whose return value is known.
    - Add the symbol # at the end of EACH block.
    - Sort imports aphabetically
 
* Performance and Safety:
    - Avoid use of global variables. If needed, use cautiously. Add suffix 
        - "_gl" to global variables
        - "_ui" to the user interface variables    
    - Code must be efficient (data-structure, functionality).
    - Avoid if-block in a loop-block unless it is required.
    - Do not calculate a common/constant value inside a loop.
    - Avoid declarations in a loop-block unless it is required.
    - Avoid initializing variables inside a loop unless it is required.
    - Initialize an array if size is known.
    - Save data in categorized folders.
    - import only the components from a package/module to be used instead of entire one.

    - Avoid using global scope
    - Prefer to use immutable types
    - Use deep-copy
    - Use [None for i in Sequence] instead of [None]*len(Sequence)
    - Initialize objects with None (null) (NOT zero) if their size is known instead of using append-like methods.
    - Operations with dataframe
        - Sort by the same column  name, and then reset index. As an example,
            grid_EntrpAll = x_trans.value_counts(subset=featureLst,normalize=True)
            reset_index().sort_values(featureLst).reset_index()
    - Utilize process logging


'''

#%% MODULE BEGINS
module_name = '<Person>'

'''
Version: <0.1>

Description:
    <Basic person class>

Authors:
    <Davidson Rock, Finn Osifala, Bryce Norris>

Date Created     :  November 12th, 2024
Date Last Updated:  November 12th, 2024

Doc:
    <***>

Notes:
    <***>
'''

#%% IMPORTS                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
   import os
   #os.chdir("./../..")
#

#custom imports


#other imports
from   copy       import deepcopy as dpcpy


from   matplotlib import pyplot as plt
import mne
import numpy  as np 
import os
import pandas as pd
import seaborn as sns
import datetime

#%% USER INTERFACE              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% CONSTANTS                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#%% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Global declarations Start Here



#Class definitions Start Here

class Person:
    
    first_name = ""
    last_name = ""
    date_of_birth = datetime.date()
    
    def __init__(self, fname, lname, dob):
        self.first_name = fname
        self.last_name = lname
        
    def toDict(self): # Stores the contents of person to a dictionary and returns it
        this_person = {
                "First Name" : self.first_name,
                "Last Name" : self.last_name,
                "Date of Birth" : self.date_of_birth
            }
        return this_person


class Employee(Person):
    
    job = ""
    employeeId = 0
    
    def __init__(self, fname, lname, dob, j):
        super().__init__(self, fname, lname)
        self.job = j
    
    def readFile(): # Reads input file and stores to dataframe
        return

#Function definitions Start Here
def main():
    pass

def plotDoB(): #Plots the date of birth for all persons (as a histogram)
    return
#

#%% MAIN CODE                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main code start here



#%% SELF-RUN                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main Self-run block
if __name__ == "__main__":
    
    print(f"\"{module_name}\" module begins.")
    
    #TEST Code
    main()