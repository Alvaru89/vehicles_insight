import pandas as pd
import numpy as np

def  my_func(x):
	return print(x.shape)

#Example:
vehicles_df=pd.read_excel('data/vehicles.xlsx')
my_func(vehicles_df)
