def beamVolLC1(material,geometry,q,l,x=0,plotStatus="only",status=" "):
    """
    Description:
    Calculates beam deflection parameters for a fixed end beam subjected to
    a distributed load in a given distance

    Parameters:
    material: material object
    geometry: profile geometry object
    q: applied distributed load
    l: Beam length
    x: end limit of the applied load

    Output:
    delta_max: beam vertical deflection in the given point
    theta_l: beam angle of tilt in the given point
    """

    if x==0:
        x = l
    k = 1/(material.E*geometry.Ix)

    def functionDelta(x):
        return -k*1/24*q*x**2*(6*l**2-4*l*x+x**2)

    delta_max = functionDelta(x)
    theta_l = 1/6*k*q*l**3
    # plot
    xv = np.linspace(0,l)
    deltaForPlot = functionDelta(xv)

    if status == "superposition":
        return [deltaForPlot,xv]

    plotter(xv,deltaForPlot,status=plotStatus,tag="DistLoadCantlieverBeam")



    return delta_max, theta_l

def beamVolLC2(material,geometria,p,l,x=0,plotStatus='only',status=" "):
    """
    Description:
    Calculates beam deflection parameters for a fixed end beam subjected to
    a point load in a given distance

    Parameters:
    material: material object
    geometry: profile geometry object
    p: applied distributed load
    l: Beam length
    x: end limit of the applied load

    Output:
    delta_max: beam vertical deflection in the given point
    theta_l: beam angle of tilt in the given point
    """

    if x==0:
        x = l
    k = 1/(material.E*geometria.Ix)

    def functionDelta(x):
        return -1/6*k*p*x**2*(3*l-x)

    delta_max= functionDelta(x)
    theta_l = 1/2*k*p*l**2
    # plot
    xv = np.linspace(0,l)
    deltaForPlot = functionDelta(xv)

    if status == "superposition":
        return [deltaForPlot,xv]

    plotter(xv,deltaForPlot,status=plotStatus,tag="PointLoadCantlieverBeam")

    return delta_max, theta_l

def beamVolLC3(material,geometria,m,l,x=0,plotStatus='only',status=" "):
    """
    Description:
    Calculates beam deflection parameters for a fixed end beam subjected to
    an applied moment

    Parameters:
    material: material object
    geometry: profile geometry object
    m: applied moment
    l: Beam length
    x: end limit of the applied load

    Output:
    delta_max: beam vertical deflection in the given point
    theta_l: beam angle of tilt in the given point
    """

    if x==0:
        x = l
    k = 1/(material.E*geometria.Ix)

    def functionDelta(x):
        return -1/2*k*m*x**2

    delta_max= functionDelta(x)
    theta_l = k*m*l
    # plot
    xv = np.linspace(0,l)
    deltaForPlot = functionDelta(xv)

    if status == "superposition":
        return [deltaForPlot,xv]

    plotter(xv,deltaForPlot,status=plotStatus,tag="MomentCantlieverBeam")


    return delta_max, theta_l

def beamSupLC1(material,geometria,q,l,x=0,plotStatus='only',status=" "):
    """
    Description:
    Calculates beam deflection parameters for a simply supported
    beam subjected to distributed load

    Parameters:
    material: material object
    geometry: profile geometry object
    q: distributed load
    l: Beam length
    x: coordinate of position along beam

    Output:
    delta_max: beam vertical deflection in the given point
    theta_l: beam angle of tilt in the given point
    """
    if x==0:
        x = l/2
    k = 1/(material.E*geometria.Ix)

    def functionDelta(x):
        return -k*1/24*q*x*(l**3-2*l*x**2+x**3)

    delta_max = functionDelta(x)
    theta_ends = 1/24*k*q*l**3
    # plot
    xv = np.linspace(0,l)
    deltaForPlot = functionDelta(xv)


    if status == "superposition":
        return [deltaForPlot,xv]

    plotter(xv,deltaForPlot,status=plotStatus,tag="DistLoadSimpSupp")

    return delta_max,theta_ends

def beamSupLC2(material,geometria,p,l,x=0,plotStatus='only',status=" "):
    """
    Description:
    Calculates beam deflection parameters for a simply supported
    beam subjected to point load

    Parameters:
    material: material object
    geometry: profile geometry object
    p: point load
    l: Beam length
    x: coordinate of position along beam

    Output:
    delta_max: beam vertical deflection in the given point
    theta_l: beam angle of tilt in the given point
    """
    if x==0:
        x = l/2
    k = 1/(material.E*geometria.Ix)

    def functionDelta(x):
        return -k*1/48*p*x*(3*l**2-4*x**2)

    delta_max = functionDelta(x)
    theta_ends = -k*p/2*(l-2*x)
    # plot
    xv = np.linspace(0,l)
    deltaForPlot = functionDelta(xv)


    if status == "superposition":
        return [deltaForPlot,xv]

    plotter(xv,deltaForPlot,status=plotStatus,tag="PointLoadSimpSupp")

    return delta_max,theta_ends

def beamSupLC3(material,geometria,p,a,l,x=0,plotStatus='only',status=" "):
    """
    Description:
    Calculates beam deflection parameters for a simply supported
    beam subjected to two symmetric loads from both ends

    Parameters:
    material: material object
    geometry: profile geometry object
    p: point load
    a: distance from ends
    l: Beam length
    x: coordinate of position along beam

    Output:
    delta_max: beam vertical deflection in the given point
    theta_l: beam angle of tilt in the given point
    """
    if x==0:
        x = l/2
    k = 1/(material.E*geometria.Ix)

    def functionDelta(x):
        return -1/6*k*p*a*(3*l*x - 3*x**2 - a**2)

    delta_max = functionDelta(x)
    theta_ends = -1/2*k*p*a*(l-2*x)

    # plot
    xv = np.linspace(0,l)
    deltaForPlot = functionDelta(xv)


    if status == "superposition":
        return [deltaForPlot,xv]

    plotter(xv,deltaForPlot,status=plotStatus,tag="SymmLoadSimpSupp")


    return delta_max,theta_ends

#--------------------CASOS VIGAS INDETERMINADAS-----------------

def beamDoubleFixedEnds(material, geometria, qw, l,plotStatus='only'):
    """
    Description:
    Calculates reactions and beam deflection for indeterminates fixed ends condition subjected
    to a distributed load

    Parameters:
    material: material object
    geometry: profile geometry object
    qw: applied distributed load
    l: Beam length

    Output:
    Ray: vertical force reactions that act on ends
    def_total: total beam vertical deflection in the given point
    Ma: Moment reaction that acts on ends
    """
    # CASO viga empotrada en dos extremos con carga distribuida aplicada
    # l = Longitud entre extremos fijados
    # qw = Carga distribuida lineal entre extremos
    beam = geometria
    E = material.E
    I = beam.Ix
    k = 1/(E*I)

    # Definición y solución de ecuaciones para carga aplicada y cargas redundantes
    a11 = 1/3*k*l**3
    a12 = 1/2*k*l**2
    a21 = 1/2*k*l**2
    a22 = k*l

    b11 = qw*1/8*k*l**4
    b21 = qw*1/6*k*l**3

    A = np.array([[a11,a12],[a21,a22]])
    B = np.array([[b11],[b21]])
    #  Solución del sistema indeterminado

    SOL = np.linalg.solve(A, B)

    Rby = SOL[0] # Reacción extremo 2 (igual a 1)
    Mb = SOL[1] # Momento Extremo 2 (igual a 1)

    Ray = qw*l-Rby
    Ma = Mb-Rby*l+qw*l**2/2

    # Cálculo de deflexión máxima por superposición de deflexiones

    (def_1,xv_1) = beamVolLC1(material, beam, qw, l,x=l/2,status="superposition")
    (def_2,xv_2) = beamVolLC2(material, beam, -Rby, l, x=l/2,status="superposition")
    (def_3,xv_3) = beamVolLC3(material, beam, Mb, l, x=l/2,status="superposition")

    xv = xv_1
    deltaForPlot = def_1+def_2-def_3
    def_total = min(deltaForPlot)

    plotter(xv,deltaForPlot,status=plotStatus,tag="FixedEnds")

    return [Ray,Ma,def_total]

