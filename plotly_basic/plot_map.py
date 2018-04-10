import os

import plotly
import plotly.plotly as py
import pandas as pd
from faker import Faker

faker = Faker()

df = pd.DataFrame([{'lat'    : faker.latitude(),
                    'long'   : faker.longitude(),
                    'country': faker.country(),
                    'state'  : faker.state(),
                    'city'   : faker.city(),
                    'name'   : faker.name(),
                    'cnt'    : faker.random_int()} for i in range(2000)])
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
df.head()

df['text'] = df['name'] + '' + df['city'] + ', ' + df['state'] + '' + 'Arrivals: ' + df['cnt'].astype(str)

scl = [[0, "rgb(5, 10, 172)"], [0.35, "rgb(40, 60, 190)"], [0.5, "rgb(70, 100, 245)"], \
       [0.6, "rgb(90, 120, 245)"], [0.7, "rgb(106, 137, 247)"], [1, "rgb(220, 220, 220)"]]

data = [dict(
    type='scattergeo',
    lon=df['long'],
    lat=df['lat'],
    text=df['text'],
    mode='markers',
    marker=dict(
        size=8,
        opacity=0.8,
        reversescale=True,
        autocolorscale=False,
        symbol='square',
        line=dict(
            width=1,
            color='rgba(102, 102, 102)'
        ),
        colorscale=scl,
        cmin=0,
        color=df['cnt'],
        cmax=df['cnt'].max(),
        colorbar=dict(
            title="Total Responses"
        )
    ))]

layout = dict(
    title='Result Sheet',
    colorbar=True,
    geo=dict(
        scope='usa',
        projection=dict(type='albers usa'),
        showland=True,
        landcolor="rgb(250, 250, 250)",
        subunitcolor="rgb(217, 217, 217)",
        countrycolor="rgb(217, 217, 217)",
        countrywidth=0.5,
        subunitwidth=0.5
    ),
)

fig = dict(data=data, layout=layout)
_path = os.path.join("/home/quixom/Desktop", 'temp.html')
plotly.offline.plot(fig, validate=False, filename=_path)
