import numpy as np
import pandas as pd
from statsmodels.tsa.seasonal import STL
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

dataframe = pd.read_csv("Data/typed_combine.csv")
dataframe['data'] = pd.to_datetime(dataframe['data'])
dataframe = dataframe.set_index('data')['receita']
dataframe = dataframe.resample('D').mean().ffill()

res = seasonal_decompose(dataframe, 'additive')
res.plot()
plt.show()

