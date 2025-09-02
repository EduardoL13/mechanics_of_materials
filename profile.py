# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

class geometry():
    # Por defecto, geometry es un perfil rectangular
    
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
        inertia: 2nd moment of area (Inertia). For a rod or a tube Ixx = Iyy
        J: Polar moment of inertia.
        units: Work units (either "SI" (m) or "IMP" (in))

        Output:
        attribute.diameter
        attribute.thkWall
        attribute.diameterInner
        attribute.areaSection
        attribute.inertia
        attribute.J
        attribute.units

        """
        self.diameter = diameter
        self.thkWall = thkWall
        diameterInner = self.diameter-2*self.thkWall
        if diameterInner == self.diameter:
            self.areaSection = np.pi*((self.diameter/2)**2)
            self.Ix = np.pi/4*((self.diameter/2)**4)
        else:
            self.areaSection = np.pi*((self.diameter/2)**2-(diameterInner/2)**2)
            self.Ix = np.pi/4*((self.diameter/2)**4 - (diameterInner/2)**4)

        self.polarMoment = self.Ix*2 # Momento polar de inercia

        #self.J
 #       self.featureDim =



class rectangular(geometry):

    def setProfile(self,width,height,thkWall=0):
        """
        Description:
        Set geometry profile and it's properties. All input parameters units must be either [m] (SI) or [in] (IMP)

        Parameters:
        diameter: Outer diameter of the tube or rod
        thkWall: Wall thickness of the tube (for a rod this value is 0)
        diameterInner: inner diameter for a tube (irrelevant in a rod)
        areaSection: Area of the geometry
        inertia: 2nd moment of area (Inertia). For a rod or a tube Ixx = Iyy
        J: Polar moment of inertia.
        units: Work units

        Output:
        attribute.diameter
        attribute.thkWall
        attribute.diameterInner
        attribute.areaSection
        attribute.inertia
        attribute.J
        attribute.units

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
            self.Ix = 1/12*self.width*self.height**3
            self.Iy = 1/12*self.height*self.width**3
        else:
            self.areaSection = areaSectionWhole - areaInner
            self.Ix = 1/12*self.width*self.height**3 - 1/12*widthInner*heightInner**3
            self.Iy = 1/12*self.height*self.width**3 - 1/12*heightInner*widthInner**3
        
class beamI(geometry):
    
    def setFlange(self,widthFlange,heightFlange):
        
        self.flange = rectangular(units = self.units)
        self.flange.setProfile(widthFlange, heightFlange)
    
    def setWeb(self,widthWeb,heightWeb):
        
        self.web = rectangular(units = self.units)
        self.web.setProfile(widthWeb, heightWeb)     
        
    def setInertiaSA(self):
        kParallelAxis = self.flange.Ix + self.flange.areaSection*(self.web.height/2 + self.flange.height/2)**2
        self.inertiaSA = self.web.Ix + kParallelAxis*2
        
    def setInertiaWA(self):
        kParallelAxis = self.flange.Iy # + self.flange.areaSection*(self.web.width/2 + self.flange.width/2)**2
        self.inertiaWA = self.web.Iy + kParallelAxis*2        
        
    def setSectionalArea(self):
        self.sectionArea = self.flange.sectionArea*2 + self.web.sectionArea
        
class beamC(geometry):
    
    def setFlange(self,widthFlange,heightFlange):
        
        self.flange = rectangular(units = self.units)
        self.flange.setProfile(widthFlange, heightFlange)
    
    def setWeb(self,widthWeb,heightWeb):
        
        self.web = rectangular(units = self.units)
        self.web.setProfile(widthWeb, heightWeb)     
        
    def setInertiaSA(self):
        kParallelAxis = self.flange.Ix + self.flange.areaSection*(self.web.height/2 + self.flange.height/2)**2
        self.inertiaSA = self.web.Ix + kParallelAxis*2
        
    def setInertiaWA(self):
        kParallelAxis = self.flange.Iy # + self.flange.areaSection*(self.web.width/2 + self.flange.width/2)**2
        self.inertiaWA = self.web.Iy + kParallelAxis*2        
        
    def setSectionalArea(self):
        self.sectionArea = self.flange.sectionArea*2 + self.web.sectionArea
        