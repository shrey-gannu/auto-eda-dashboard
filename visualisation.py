import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
# %matplotlib inline
def cat_vis(df,xl):
    fig,ax = plt.subplots(figsize = (4,4))
    p=sns.countplot(data=df, x=xl,ax = ax)
    return p
def num_vis(df,xl):
    fig,ax = plt.subplots(figsize = (4,4))
    sns.histplot(data=df, x=xl, palette= 9 , kde=True,ax=ax)
    return ax
def tab3_vis(df,xl,yl):
    sns.relplot(data=df, x=xl, y=yl ,palette= 9)
    return None
def tab4_viz(df,xl,yl,zl):
    sns.relplot(data=df, x=xl, y=yl, hue=zl)
    return None


