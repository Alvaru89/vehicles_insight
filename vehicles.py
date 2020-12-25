import pandas as pd
import numpy as np

def  my_func(x):
	print(f'Data frame shape is {x.shape}')
	print(f'Data frame length is  {len(x.T.columns.tolist())}')
	print(f'Columns are: {x.columns}')
	return
#Example:
vehicles_df=pd.read_excel('data/vehicles.xlsx')
my_func(vehicles_df)
