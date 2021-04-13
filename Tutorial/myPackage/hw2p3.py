import pandas as pd
def twice(df):
    df.iloc[:,1]=df.iloc[:,1].apply(lambda x: 2*x)
    return df
def isOk(x):
    x = float(x)
    if(x<2 and x>-2):
        print('Acceptable')
    else:
        if(x<=-2):
            print('Too small')
        else:
            print('Too big')