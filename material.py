# -*- coding: utf-8 -*-
"""
material module

Description: Sets material object that imports material data from the data hub (excel file) used for engineering calculations done in the EE Module

@author: ELC
"""

import numpy as np
import pandas as pd

materialData = 'C:\\\\Users\\\\ELC\\\\Documents\\\\ModulesEL\\\\englib\\\\Material.xlsx'


class material():

    
    def __init__(self, material="Al2014 T6",sheetName = "METAL SI"):
       """
       -Description:
       Initiates a material object with it's properties for a specified material
       -Input Parameters:
       material Type: String
       sheetName Type String
       -Output:
       Material object with data extracted from the excel file (Data Hub)
       """
       materialDF = pd.read_excel(materialData,index_col="Material",sheet_name=sheetName)
       self.name = material
       self.youngModulus = materialDF.loc[material,"Young Modulus"]
       self.density = materialDF.loc[material,"Density"]
       self.yieldStrength = materialDF.loc[material,"Yield Strength"]
       self.ultimateStrength = materialDF.loc[material,"Ultimate Strength"]
       self.poisson = materialDF.loc[material,"Poisson Ratio"]
    
    
    
    
    


        

