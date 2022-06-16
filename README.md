<h1 align= "center">Dashboard Racconn Monks</h1>


A repo with the aim of showcase my data analysis with Python/SQL/Sheets and deploy a dashboard created with StreamLit.

<h1 align= "center">Test Case 1</h1>

[Clique aqui para ver o Dashboard!](https://share.streamlit.io/clessonr/raccoontestcase/main/TestCase_1/Dashboard/%F0%9F%93%9D_Dashboard.py)

Logo ao ler a questão fornecida, apliquei a filosofia da qual aprendi no Google, que serve amplamente para qualquer análise de dados (APPASA) Ask, Prepare, Processe, Analyse, Share e Act, então tive o brainstorm. 
Observando os dados, já pude notar que existiam dois grupos de dados a serem analisados, dados antes do blog e dados após seu lançamento, imediatamente pensei em duas abordagens, previsão de vendas com a existência e sem a existência do blog e provas que mostrem se o blog teve algum impacto, caso sim qual foi ele? De que forma esse impacto pode ser mensurado? Primeiramente começarei com um Teste de Hipótese (Two-Sample T Test) supondo que a hipótese nula é que o blog não interfere em nada no site de maneira geral, também adotarei um p-value de 5%. 

As informações foram mais do que esclarecedoras e pude notar que o resultado ficou extremamente abaixo de um p-value científico (0.01), então já estava mais que provado que algum impacto foi causado na base de dados, porém optei por não adicionar ao dashboard. 
Seguindo a investigação pensei nos 3  indicadores que iriam me render os melhores insights, cheguei a conclusão que usaria decomposição, por se tratar de renda e existirem vários fatores que podem gerar ruído  ou não, além de sazonalidades, média móvel que eventualmente se tornou num gráfico de tendência para observar que rumo as vendas da marca tomariam considerando o período. 

Para resultados mais concretos em relação à uma possível lógica de crescimento, e que só decidi utilizar após ter os resultados da regressão, p-value e das tendências, foi a regressão, que mostrou de forma perfeita o quão gritante foi o impacto do blog. Além de todos esses métodos estatísticos clássicos, também calculei qual porcentagem dos usuários do blog realizaram algum tipo de transação, e qual porcentagem dos usuários do site realizaram algum tipo de transação, novamente o insight foi gritante tendo uma grande margem percentual a frente do site, quando o blog é o ponto de comparação, e assim construir meu dashboard final a partir do StreamLit, usei tal ferramenta por acreditar fortemente que clientes se sintam mais familiares com interfaces web atualmente e também ter uma maior familiaridade. 

Em relação à linguagem de programação o Python foi utilizado  juntamente às suas bibliotecas Numpy, Pandas, Statsmodels, Matplotlib e Scipy, todas utilizadas para fazer o plot e o cálculo de cada gráfico.

---
<h1 align= "center">Test Case 2</h1>
For this part of the case I basically used PostgreSQL with Microsoft SQL Server Management Studio.
For a more in depth explanation of the case, please see the .sql file itself.


