import numpy as np
import pandas as pd
import scipy.stats as stats


dataframe = pd.read_csv("Dashboard/Data/typed_combine.csv")

def to_bit(dataframe):
    "Transforms types into bit 1 or 0"
    if dataframe["type"] == "bs":
        return 1
    else:
        return 0

dataframe["type"] = dataframe.apply(to_bit, axis=1) # Applying the data transformations

#? A Two Sample T-test will be realized in order to check if revenue and site transactions means are equal to zero.

dataframe_a = dataframe[dataframe["type"] > 0] # Selecting the first datagroup
dataframe_b = dataframe[dataframe["type"] < 1] # Selecting the second datagroup

revenue_a = dataframe_a["receita"]
revenue_b = dataframe_b["receita"]
ratio_check_a = np.var(revenue_a)/np.var(revenue_b) # Checking if both populations are normally distributed.
print(stats.ttest_ind(revenue_a, revenue_b, equal_var=True))


transactions_a = dataframe_a["transacoes_site"]
transactions_b = dataframe_b["transacoes_site"]
ratio_check_b = np.var(transactions_a)/np.var(transactions_b)
print(stats.ttest_ind(transactions_a, transactions_b, equal_var=True))

#? As the two pvalue are way less than 0.05, we can conclude that the means of the two populations are not equal, consequently
#?  the mean of both samples are not equal, something has changed the behaviour.
