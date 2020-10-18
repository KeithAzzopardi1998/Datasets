import numpy as np
import pandas as pd

#the basic idea is to represent an instance as two dataframes,
#one for the customers (c_df) and another for the vehicles (v_df)
def loadInstance(filename,debug=False):
    if debug: print("DEBUG: loading instance from",filename)

    df = pd.read_csv(filename,
        delimiter='\t',
        names=['id','origin','destination','quantity','early'])
    if debug: print("DEBUG: loaded instance data with %d entities"%len(df))
    
    c_df=df[df.quantity>0].copy()
    if debug: print("DEBUG: instance contains %d customers"%len(c_df))    

    v_df=df[df.quantity<0].copy()
    if debug: print("DEBUG: instance contains %d vehicles"%len(v_df))
    v_df['quantity']=v_df['quantity'].multiply(-1)

    return c_df,v_df

def saveInstance(filename,c_df,v_df):
    
    v_df['quantity']=v_df['quantity'].multiply(-1)

    df = pd.concat([v_df, c_df], ignore_index=True)
    df=df.astype(int)
    df.to_csv(filename,
        sep='\t',
        index=False,
        header=False)

if __name__ == "__main__":
    customers, vehicles = loadInstance('Manhattan/mny-1-5000.instance',debug=True)
    vehicles['quantity']=10
    saveInstance('Manhattan/temp.instance',customers,vehicles)