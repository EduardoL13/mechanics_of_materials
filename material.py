# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 14:33:56 2025

@author: ELC
"""

import numpy as np
import pandas as pd

materialData = 'C:\\\\Users\\\\ELC\\\\Documents\\\\ModulesEL\\\\englib\\\\Material.xlsx'


class material():
    
    def __init__(self, material="Al2014 T6",sheetName = "METAL SI"):
        
       materialDF = pd.read_excel(materialData,index_col="Material",sheet_name=sheetName)
       self.name = material
       self.youngModulus = materialDF.loc[material,"Young Modulus"]
       self.density = materialDF.loc[material,"Density"]
       self.yieldStrength = materialDF.loc[material,"Yield Strength"]
       self.ultimateStrength = materialDF.loc[material,"Ultimate Strength"]
       self.poisson = materialDF.loc[material,"Poisson Ratio"]
    
    
    
    
    

        