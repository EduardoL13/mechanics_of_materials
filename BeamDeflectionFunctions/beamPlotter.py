import matplotlib.pyplot as plt

def plotter(dataX,dataY,status="only",tag=" "):
    if status == "only":
        plt.figure(figsize =(8,3))
        plt.plot(dataX,dataY,lw = 1.5, color = 'b')
        plt.xlabel('Distance [m]')
        plt.ylabel('Deflectión [m]')
        plt.grid()
        plt.xlim(0,1.1*dataX[-1]) # Límites del display de la ventana en X
        plt.ylim(-abs(min(dataY))*2,2*abs(min(dataY))) # Límites del display de la ventana en y
        plt.title("Beam deflection")
        plt.show()
    elif status == "first":
        plt.figure(figsize =(8,3))
        plt.plot(dataX,dataY,label=tag,lw = 1.5, color = 'r')
        plt.xlabel('Distance [m]')
        plt.ylabel('Deflectión [m]')
        plt.grid()
        plt.xlim(0,1.1*dataX[-1]) # Límites del display de la ventana en X
        plt.ylim(-abs(min(dataY))*2,2*abs(min(dataY))) # Límites del display de la ventana en y
        plt.title("Beam deflection")
    elif status == "last":
        plt.plot(dataX,dataY,label=tag,lw = 1.5, color = 'g')
        plt.legend(loc = 'upper right', fontsize = 8 ,ncol=2)
        plt.show()
