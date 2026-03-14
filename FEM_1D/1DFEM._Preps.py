import numpy as np
import sys
from sympy import symbols, integrate, sin, exp, oo, diff

x = symbols('x')

#def kEval(E,A,derPhiFun1,derPhiFun2,step):
#    return E*A*derPhiFun1*derPhiFun2*step

# genTerm = lambda x: x # Acá se define la carga distribuída si la hay o el término de "generación de energía"

def kEval(E,A,derPhiFun1,derPhiFun2):
    return E*A*derPhiFun1*derPhiFun2

def fillResult(placeHolderList,eliminatedRows,listOfNodes,partialSolution,result=[]):
    if len(placeHolderList) == 0:
        return result
    elif placeHolderList[0] != 0:
        result.append(listOfNodes[eliminatedRows[0]].EBC)
        return fillResult(placeHolderList[1:],eliminatedRows[1:],listOfNodes,partialSolution,result)
    else:
        result.append(partialSolution[0,0])
        return fillResult(placeHolderList[1:],eliminatedRows,listOfNodes,partialSolution[1:],result)


### Input Term ###
genTerm = x
genTermSpec = "per length"



##################

def fEval(genTerm,phiFun,A=1):
    return genTerm*phiFun*A    # A se especifica dependiendo de la expresión del genTerm

class nodeFE():
    def __init__(self, position, label):
        self.position = position
        self.label = label

    def setEBC(self,value):
        self.EBC = value

    def setNBC(self,value):
        self.NBC = value

class elementFE():

    def __init__(self, startNode, endNode, stepSize, label):

        self.startNode = startNode #
        self.endNode = endNode #
        self.stepSize = stepSize #
        self.label = label

    def setCoeffShape(self):
        #shapeSN = lambda x : 1-(x-self.startNode.position)/(self.stepSize)
        #shapeEN = lambda x : (x-self.startNode.position)/(self.stepSize)
        shapeSN = 1-(x-self.startNode.position)/(self.stepSize)
        shapeEN = (x-self.startNode.position)/(self.stepSize)
        #dPhiSN = -1/self.stepSize
        #dPhiEN = 1/self.stepSize
        dPhiSN = diff(shapeSN,x)
        dPhiEN = diff(shapeEN,x)

        self.dPhiSN = dPhiSN
        self.dPhiEN = dPhiEN
        self.shapeSN = shapeSN
        self.shapeEN = shapeEN
