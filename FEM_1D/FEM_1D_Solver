# HC
import numpy as np

# Definición de step size (De donde se definirán después los nodos y elementos)
hVec = [20,40,40] #[cm]
length = sum(hVec)

# Definición parámetros geométricos y de material

E = 5*10**7 # [N/cm**2]
A0 = 10 #[cm**2]
areaSec = A0*(2-x/length) #[m**2]


# Definición de nodos y elementos
noElements = len(hVec)
noNodes = noElements + 1


posVec = [sum(hVec[:i]) for i in range(len(hVec)) ]#for i,val in enumerate (hVec)]
posVec.append(sum(hVec))
#print(posVec)

listElements = []
listNodes = []

for i in range(len(posVec)):
    listNodes.append(nodeFE(posVec[i], i+1))
    #print("Created Node ", listNodes[i].label)
    #print("Situated at ", posVec[i])

# Definición de Boundary conditions
listNodes[0].setEBC(0)
listNodes[-1].setEBC(0.05)

for i in range(noElements):
    listElements.append(elementFE(listNodes[i], listNodes[i+1], hVec[i], i+1))
    listElements[i].setCoeffShape()
 #   print("Created Element: ", listElements[i].label)
 #   print("with Start node: ", listElements[i].startNode.label)
 #   print("and End node: ", listElements[i].endNode.label)
 #   print("with phi_2 at End  = ", listElements[i].shapeEN(listElements[i].endNode.position))



kMatrix = np.zeros([noNodes, noNodes])
fVec = np.zeros([noNodes,1])
#dResultVec = np.zeros([noNodes,1])
phVec = [0 for i in range(noNodes)]

colRowToEliminate = [] # inicialización vector para método eliminación

for node in range(noElements):

    # Llenado de matriz K
    k_ss = kEval(E,areaSec,listElements[node].dPhiSN,listElements[node].dPhiSN) #dphi1*dphi1
    k_se = kEval(E,areaSec,listElements[node].dPhiSN,listElements[node].dPhiEN) #dphi1*dphi2
    k_ee = kEval(E,areaSec,listElements[node].dPhiEN,listElements[node].dPhiEN) #dphi2*dphi2

    kMatrix[node, node] += integrate(k_ss,x).subs(x,listElements[node].endNode.position - listElements[node].startNode.position)
    kMatrix[node, node+1] += integrate(k_se,x).subs(x,listElements[node].endNode.position - listElements[node].startNode.position)
    kMatrix[node+1, node] += kMatrix[node, node+1]
    kMatrix[node+1, node+1] += integrate(k_ee,x).subs(x,listElements[node].endNode.position - listElements[node].startNode.position)

    #print("k_matrix[node] = ", kMatrix[node,node])

    # Definición de término de gen term del load vector
    if genTermSpec == "per volume":
        f_1e = fEval(genTerm,listElements[node].shapeSN,areaSec)
        f_2e = fEval(genTerm,listElements[node].shapeEN,areaSec)
    else:
        f_1e = fEval(genTerm,listElements[node].shapeSN)
        f_2e = fEval(genTerm,listElements[node].shapeEN)

    #print("f1e = ",integrate(f_1e,x).subs(x,listElements[node].endNode.position - listElements[node].startNode.position))
    #print("f_vec[node] = ", fVec[node,0])

    # Evaluación de natural boundary conditions (NBC) y llenado de f
    if hasattr(listElements[node].startNode, 'NBC'):
        fVec[node] += integrate(f_1e,x).subs(x,listElements[node].endNode.position - listElements[node].startNode.position) + listElements[node].NBC #
        fVec[node+1] += integrate(f_2e,x).subs(x,listElements[node].endNode.position - listElements[node].startNode.position)
    if listElements[node] == listElements[-1]:
        if hasattr(listElements[node].endNode, 'NBC'):
            fVec[node] += integrate(f_1e,x).subs(x,listElements[node].endNode.position - listElements[node].startNode.position)  #
            fVec[node+1] += integrate(f_2e,x).subs(x,listElements[node].endNode.position - listElements[node].startNode.position) + listElements[node].NBC
    else:
        fVec[node,0] += integrate(f_1e,x).subs(x,listElements[node].endNode.position - listElements[node].startNode.position)  #
        fVec[node+1,0] += integrate(f_2e,x).subs(x,listElements[node].endNode.position - listElements[node].startNode.position)


# Evaluación de essential boundary conditions (EBC) (eliminación)
    if hasattr(listElements[node].startNode, 'EBC'):
        colRowToEliminate.append(listElements[node].startNode.label-1)
        #print("appended : ",listElements[node].startNode.label)
        fVec[node+1,0] += E*areaSec*listElements[node].startNode.EBC ### CONFIRMAR SI ESTE ES EL UNICO CAMBIO DEBIDO A LAS EBC EN EL VECTOR F

    if listElements[node] == listElements[-1]:
        if hasattr(listElements[node].endNode, 'EBC'):
            colRowToEliminate.append(listElements[node].endNode.label-1) #
            #print("appended : ",listElements[node].endNode.label)

#print("Previous K Matrix = ", kMatrix)
#print("Previous f Vector = ", fVec)

# Creación de placeholders en dResult
for val in colRowToEliminate:
    phVec[val] = "p" #  p es el place holder

#print("placeholder = ", phVec)


if colRowToEliminate:
    kMatrix = np.delete(kMatrix,colRowToEliminate,axis=0) # Elimina filas
    kMatrix = np.delete(kMatrix,colRowToEliminate,axis=1) # Elimina colummnas
    fVec = np.delete(fVec,colRowToEliminate,axis=0) # Elimina filas

#print(colRowToEliminate)
print("K Matrix = ", kMatrix/(E*A0))

dSolWithoutEBC = np.linalg.solve(kMatrix, fVec)

dSol = []
dSol = fillResult(phVec,colRowToEliminate,listNodes,dSolWithoutEBC,dSol)
dSol = np.array(dSol).reshape(-1, 1)

print("Load Vector = ", fVec)
print("Full Displacements soution = ", dSol)
