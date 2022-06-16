import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


data = pd.read_csv("Dashboard/Data/before_blog.csv")
data2 = pd.read_csv("Dashboard/Data/after_blog_combined.csv")

y = data["receita"]
x = data["transacoes_site"]

y2 = data2["receita"]
x2 = data2["transacoes_site"]


plt.scatter(x, y, color="red", label="Before")
plt.scatter(x2, y2, color="blue", label="After")

slope, intercept, r, p, std_err = stats.linregress(x, y)
slope2, intercept2, r2, p2, std_err2 = stats.linregress(x2, y2)

def myfunc(x):
  return slope * x + intercept

def myfunc_2(x2):
  return slope2 * x2 + intercept2


mymodel = list(map(myfunc, x))
mymodel_2 = np.array(x.values)*slope2 +intercept2

plt.plot(x, mymodel, color = "red")
plt.plot(x, mymodel_2, color = "blue")

plt.show()
