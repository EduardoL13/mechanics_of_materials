# -*- coding: utf-8 -*-
"""
geometry module

Description: Sets custom geometry object used for engineering calculations done in the EE Module

@author: ELC
"""

import numpy as np

class geometry():
    
    def __int__(self, units = "SI"):
        self.units = units
        print("Units set to " + self.units)
    
    def units(self):
        """
        Description:
        Return work units in the console

        Parameters: none

        Output: none
        """
        print(self.units)

class circular(geometry):
    
    def setProfile(self,diameter,thkWall=0):
        """
        Description:
        Set geometry profile and it's properties. All input parameters units must be either [m] (SI) or [in] (IMP)

        Parameters:
        diameter: Outer diameter of the tube or rod
        thkWall: Wall thickness of the tube (for a rod this value is 0)
        diameterInner: inner diameter for a tube (irrelevant in a rod)
        areaSection: Area of the geometry
        inertia_xx: 2nd moment of area x (Ixx). 
        inertia_yy: 2nd moment of area y (Iyy). same value as inertia_xx in this case
        polarMoment: Polar moment of inertia.
        

        Output:
        attribute: .diameter
        attribute: .thkWall
        attribute: .areaSection
        attribute: .inertia
        attribute: .yNeutralAxis
        attribute: .polarMoment
        

        """
        self.diameter = diameter
        self.thkWall = thkWall
        diameterInner = self.diameter-2*self.thkWall
        if diameterInner == self.diameter:
            self.areaSection = np.pi*((self.diameter/2)**2)
            self.inertia_xx = np.pi/4*((self.diameter/2)**4)
        else:
            self.areaSection = np.pi*((self.diameter/2)**2-(diameterInner/2)**2)
            self.inertia_xx = np.pi/4*((self.diameter/2)**4 - (diameterInner/2)**4)

        self.yNeutralAxis = self.diameter/2
        self.polarMoment = self.Ix*2 # Momento polar de inercia

        #self.J
 #       self.featureDim =



class rectangular(geometry):

    def setProfile(self,width,height,thkWall=0):
        """
        Description:
        Set geometry profile and it's properties. All input parameters units must be either [m] (SI) or [in] (IMP)

        Parameters:
        width: Rectangular bar section width
        height: Rectangular bar section height
        thkWall: Wall thickness of the tube (for a rod this value is 0)
        areaSection: Area of the geometry
        inertia_xx: 2nd moment of area x (Ixx). 
        inertia_yy: 2nd moment of area y (Iyy). 
        
        Output:
        attribute: .width
        attribute: .height
        attribute: .thkWall
        attribute: .areaSection
        attribute: .yNeutralAxis
        attribute: .inertia_xx
        attribute: .inertia_yy
        """
        self.width = width
        self.height = height
        self.thkWall = thkWall
        areaSectionWhole = self.height * self.width

        heightInner = height-2*self.thkWall
        widthInner = width-2*self.thkWall
        areaInner = heightInner*widthInner
        if areaInner == self.height*self.width:
            self.areaSection = areaSectionWhole
            self.inertia_xx = 1/12*self.width*self.height**3
            self.inertia_yy = 1/12*self.height*self.width**3
        else:
            self.areaSection = areaSectionWhole - areaInner
            self.inertia_xx = 1/12*self.width*self.height**3 - 1/12*widthInner*heightInner**3
            self.inertia_yy = 1/12*self.height*self.width**3 - 1/12*heightInner*widthInner**3
        self.yNeutralAxis = self.height/2
        
class beamI(geometry):

    def setFlange(self,widthFlange,heightFlange):
        """
        Description:
        Flange object created by using the rectangular class object and setting required attributes
        
        Parameters
        widthFlange: width of the flange rectangular object
        heightFlange: height of the flange rectangular object
        
        Output:
        attribute: .flange
        """ 
        
        self.flange = rectangular(units = self.units)
        self.flange.setProfile(widthFlange, heightFlange)
    
    def setWeb(self,widthWeb,heightWeb):
        """
        Description:
        Web object created by using the rectangular class object and setting required attributes

        Parameters
        widthWeb: width of the Web rectangular object
        heightWeb: height of the rectangular object
        
        Output:
        attribute: .web
        """ 
        self.web = rectangular(units = self.units)
        self.web.setProfile(widthWeb, heightWeb)     
        
    def setInertiaSA(self):
        """
        Description:
        Sets inertia for beam strong axis (Ixx in this case)
        
        Output:
        attribute: .inertia_xx
        """ 
        
        kParallelAxis = self.flange.inertia_xx + self.flange.areaSection*(self.web.height/2 + self.flange.height/2)**2
        self.inertia_xx = self.web.inertia_xx + kParallelAxis*2
        
    def setInertiaWA(self):
        """
        Description:
        Sets inertia for beam weak axis (Iyy in this case)
        
        Output:
        attribute: .inertia_yy
        """         
        kParallelAxis = self.flange.inertia_yy # + self.flange.areaSection*(self.web.width/2 + self.flange.width/2)**2
        self.inertia_yy = self.web.inertia_yy + kParallelAxis*2        
        
    def setSectionalArea(self):
        """
        Description:
        Sets Area of the whole beam section 
        
        Output:
        attribute: .areaSection
        """       
        self.areaSection = self.flange.areaSection*2 + self.web.areaSection

    def setDistYNeutralAxis(self):
        """
        Description:
        Sets distance y from neutral axis xx to the furthest point in the section (top/bottom)
        
        Output:
        attribute: .yNeutralAxis
        """       
        self.yNeutralAxis = self.flange.height + self.web.height/2


class beamC(geometry):

    def setFlange(self,widthFlange,heightFlange):
        """
        Description:
        Flange object created by using the rectangular class object and setting required attributes
        
        Parameters
        widthFlange: width of the flange rectangular object
        heightFlange: height of the flange rectangular object
        
        Output:
        attribute: .flange
        """         
        self.flange = rectangular(units = self.units)
        self.flange.setProfile(widthFlange, heightFlange)
    
    def setWeb(self,widthWeb,heightWeb):
        """
        Description:
        Web object created by using the rectangular class object and setting required attributes

        Parameters
        widthWeb: width of the Web rectangular object
        heightWeb: height of the rectangular object
        
        Output:
        attribute: .web
        """         
        self.web = rectangular(units = self.units)
        self.web.setProfile(widthWeb, heightWeb)     
        
    def setInertiaSA(self):
        """
        Description:
        Sets inertia for beam strong axis (Ixx in this case)
        
        Output:
        attribute: .inertia_xx
        """ 
        kParallelAxis = self.flange.inertia_xx + self.flange.areaSection*(self.web.height/2 + self.flange.height/2)**2
        self.inertiaSA = self.web.inertia_xx + kParallelAxis*2
        
    def setInertiaWA(self):
        """
        Description:
        Sets inertia for beam weak axis (Iyy in this case)
        
        Output:
        attribute: .inertia_xx
        """ 
        kParallelAxis = self.flange.Iy # + self.flange.areaSection*(self.web.width/2 + self.flange.width/2)**2
        self.inertiaWA = self.web.Iy + kParallelAxis*2        
        
    def setSectionalArea(self):
        self.sectionArea = self.flange.sectionArea*2 + self.web.sectionArea

        




