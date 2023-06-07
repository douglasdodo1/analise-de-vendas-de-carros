import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dados\empresa_x.csv')
df['mes'] = pd.to_datetime(df['mes'])
df['aumento'] = df['vendas'].diff()
df['aceleração'] = df['aumento'].diff()

graphsList = []
titles = ['Vendas de carros entre 2017 a 2018', 'Aumento das vendas de carros entre 2017 a 2018', 
          'Aceleração de vendas de carros entre 2017 a 2018']

for col in df.columns:
    graphsList.append(col)

def plotgraph(titulo, xlabelname, ylabelname,dataset):
    plt.plot(dataset[xlabelname],dataset[ylabelname])
    plt.xlabel(xlabelname)
    plt.ylabel(ylabelname) 
    plt.title(titulo)
    plt.show()

def groupPlots(graphs,titlenames ,dataset):
    fig, axes = plt.subplots(nrows=3,ncols=1)
    for i in range(1, len(graphs)): 
        axes[i-1].plot(dataset[graphs[0]], dataset[graphs[i]], color='red', linestyle='--')
        axes[i-1].set_title(titlenames[i-1])
        axes[i-1].set_xlabel(graphs[0])
        axes[i-1].set_ylabel(graphs[i])
        axes[i-1].grid(True)

    plt.tight_layout()
    plt.show()
    


groupPlots(graphsList,titles,df)

