import os
import random

import plotly
import plotly.graph_objs as go

import pandas as pd
from faker import Faker

faker = Faker()

df_sample = pd.read_csv('https://raw.githubusercontent.com/gahan9/DSA_lab/51caebe72037acdc9fe8db87c0d8e4d456d5b9ca/sort/analysis.csv')

colorscale = ["#f7fbff", "#ebf3fb", "#deebf7", "#d2e3f3", "#c6dbef", "#b3d2e9", "#9ecae1",
              "#85bcdb", "#6baed6", "#57a0ce", "#4292c6", "#3082be", "#2171b5", "#1361a9",
              "#08519c", "#0b4083", "#08306b"]
color = ["#ff7c00", "#a91f78", "#0432ff", "#00a643", "#a6f900", "#fffb00", "#ffd300", "#c8e000"]
df_sample = df_sample.loc[df_sample['log10(DATA_SET)'] != 4.69]
df_algos = {}
dfs = {}
data = []
for algo_name in set(df_sample['ALGORITHM'].tolist()):
    df_filtered = df_sample.loc[df_sample['ALGORITHM'] == algo_name]
    df_algos[algo_name] = df_filtered
    cnt = 0
    for name, df in dfs.items():
        x = df_filtered['log10(DATA_SET)'].tolist()
        # text = df_sample['ALGORITHM'].tolist()
        algo = [i.split('_')[0] for i in df_filtered['ALGORITHM'].tolist()]
        y = [i * 1000 for i in df_filtered['TIME'].tolist()]
        xx = list('_'.join(map(str, i)) for i in zip(algo, df_filtered['DATA_SET_TYPE'].tolist()))
        ht = list('-'.join(map(str, i)) for i in zip(x, y))
        data += [go.Scatter(x=x, y=y, text=xx, hovertext=ht, name=name, marker=dict(color=color[cnt]))]
        cnt += 1
# dfs['ascending'] = df_sample.loc[df_sample['DATA_SET_TYPE'] == ' ascending']
# dfs['descending'] = df_sample.loc[df_sample['DATA_SET_TYPE'] == ' descending']
# dfs['random'] = df_sample.loc[df_sample['DATA_SET_TYPE'] == ' random']
# dfs['same'] = df_sample.loc[df_sample['DATA_SET_TYPE'] == ' same']

layout = go.Layout(title='titlE', barmode='group',
                   xaxis={'title': 'algorithm and dataset type', 'tickformat': ',d'},
                   yaxis={'title': 'time (ms)', 'tickformat': ',d'})
_path = os.path.join(".", 'temp.html')
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, validate=False, auto_open=False, filename=_path)
