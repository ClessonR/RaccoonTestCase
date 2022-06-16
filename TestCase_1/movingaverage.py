import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dashboard/Data/full_data.csv", index_col='data', parse_dates=True)


df.drop(["transacoes_blog",
                        "transacoes_site",
                        "usuarios_blog",
                        "usuarios_site"], axis=1, inplace=True)

df.plot(color='green', linewidth=3, figsize=(12,6))
df['receita'].rolling(window=72).mean().plot()

print(df['receita'].rolling(window=72).mean())

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend()

plt.title('The average revenue per day')
plt.xlabel("Date")
plt.ylabel('Revenue [R$]')
plt.show()