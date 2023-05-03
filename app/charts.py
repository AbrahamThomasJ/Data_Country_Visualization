#%%
import matplotlib.pyplot as plt # plt es un sinonimo para usar la libreria de forma mas facil
import numpy as np

 # %%


def generate_bar_chart(name,labels,values):
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.savefig(f'./countries_imgs/{name}.png')
    plt.close()

def generate_pie_chart(name,labels,values):
    fig,ax = plt.subplots()
    ax.pie(values,labels=labels)
    ax.axis('equal')
    plt.savefig(f'./continents_imgs/{name}.png')
    plt.close()


if __name__ == '__main__':
    pass
    
