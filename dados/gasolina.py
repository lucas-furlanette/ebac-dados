import pandas as pd
import seaborn as sns

g_data = pd.read_csv("dados/gasolina.csv")
g_df = pd.DataFrame(g_data)

with sns.axes_style('whitegrid'):
    grafico = sns.lineplot(data=g_df, x="dia", y="venda", palette="pastel")
    grafico.set(title='Preço médio da gasolina em SP', xlabel='Dia', ylabel='Preço R$')
    grafico.get_figure().savefig('dados/gasolina.png')
