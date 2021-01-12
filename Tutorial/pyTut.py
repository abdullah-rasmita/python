import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def add1(df):
    df.iloc[:,0]=df.iloc[:,0].apply(lambda x: x+1)
    return df
def setDefault():
    """
    Setting default setup for drawing the figure
    """
    mpl.rcParams['font.family'] = 'Arial'
    plt.rcParams['font.size'] = 18
    plt.rcParams['axes.linewidth'] = 2
def linFit(df):
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]
    fitParam, fitErr = curve_fit(lambda x,a,b: a*x+b, x, y)
    yFit = list(fitParam[0]*np.array(x)+fitParam[1])
    df['yFit'] = yFit
    print('slope: '+ "%.2f" % fitParam[0])
    print('offset: '+ "%.2f" % fitParam[1])
    setDefault()
    fig = plt.figure(figsize=(3.8, 3))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.plot(x,y,'ko')
    ax.plot(x,yFit,'r-')
    return df
def createRandom():
    x = np.linspace(start=-10, stop=10, num=200)
    y = 5.2*x+10.8+10*(np.random.rand(x.size)-0.5)
    df = pd.DataFrame(data={'x':list(x),'y':list(y)})
    df.to_csv('data/hw2Input.csv',index=False)




