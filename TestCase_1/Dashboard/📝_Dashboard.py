import streamlit as st
import numpy as np
import pandas as pd
from statsmodels.tsa.seasonal import STL
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
from scipy import stats
from PIL import Image
import os

st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
plt.style.use('ggplot')

st.markdown("<h1 style='text-align: center; color: white;'>Dashboard Raccoon Monks</h1>", unsafe_allow_html=True)
# Print current working directory and list all files
st.write("Current working directory:", os.getcwd())
st.write("Files in current directory:", os.listdir())


st.markdown("---")

col1, col2= st.columns(2)



with col1:
    st.markdown("<h1 style='text-align: center; color: white;'>Comportamento da Receita</h1>", unsafe_allow_html=True)
    # Define the relative path to the CSV file
    file_path = os.path.join("TestCase_1", "Dashboard", "Data", "full_data.csv")
    df = pd.read_csv(file_path, index_col='data', parse_dates=True)


    df.drop(["transacoes_blog",
                            "transacoes_site",
                            "usuarios_blog",
                            "usuarios_site"], axis=1, inplace=True)

    fig, ax = plt.subplots(figsize=(15, 7))
    ax = plt.plot(df.index, df.receita)
    plt.xlabel("Data")
    plt.ylabel('Receita [R$]')



    st.pyplot(fig)

    st.markdown("<h1 style='text-align: center; color: white;'>Tendência da Receita</h1>", unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(15, 7))
    ax = plt.plot(df.index, df['receita'].rolling(window=72).mean())
    plt.xlabel("Data")
    plt.ylabel('Tendência')


    st.pyplot(fig)

with col2:
    st.markdown("<h1 style='text-align: center; color: white;'>Regressão de Receita p. Transação</h1>", unsafe_allow_html=True)

    def myfunc(x):
        return slope * x + intercept

    def myfunc_2(x2):
        return slope2 * x2 + intercept2
    file_path_blog = os.path.join("TestCase_1", "Dashboard", "Data", "before_blog.csv")
    file_path_blog_combined = os.path.join("TestCase_1", "Dashboard", "Data", "after_blog_combined.csv")
    data = pd.read_csv(file_path_blog)
    data2 = pd.read_csv(file_path_blog_combined)

    y = data["receita"]
    x = data["transacoes_site"]

    y2 = data2["receita"]
    x2 = data2["transacoes_site"]

    fig, ax = plt.subplots(figsize=(15, 7))
    ax.scatter(x, y, color="red", label="Antes do Blog")
    ax.scatter(x2, y2, color="blue", label="Após o Blog")

    slope, intercept, r, p, std_err = stats.linregress(x, y)
    slope2, intercept2, r2, p2, std_err2 = stats.linregress(x2, y2)

    mymodel = list(map(myfunc, x))
    mymodel_2 = np.array(x.values)*slope2 +intercept2
    ax.plot(x, mymodel, color = "red")
    ax.plot(x, mymodel_2, color = "blue")
    plt.legend()
    plt.xlabel("Transações")
    plt.ylabel('Receita [R$]')

    st.pyplot(fig)

    st.markdown("<h1 style='text-align: center; color: white;'>Usuários que realizaram alguma transação</h1>",unsafe_allow_html=True)

    image = Image.open("/app/raccoontestcase/TestCase_1/Dashboard/Data/users.png")

    st.image(image,use_column_width=True )

st.markdown("---")

col3, col4,col5 = st.columns([1,3,1])



with col4:
    st.markdown("<h1 style='text-align: center; color: white;'>Decomposição</h1>",unsafe_allow_html=True)

    dataframe = pd.read_csv("/app/raccoontestcase/TestCase_1/Dashboard/Data/typed_combine.csv")
    dataframe['data'] = pd.to_datetime(dataframe['data'])
    dataframe.rename(columns = {'receita':'Receita ao longo do tempo'}, inplace = True)
    dataframe = dataframe.set_index('data')['Receita ao longo do tempo']
    dataframe = dataframe.resample('D').mean().ffill()
    res = seasonal_decompose(dataframe, 'additive')
    fig = res.plot()
    fig.set_size_inches((16, 9))
    st.pyplot(fig, figsize=(1,1))




