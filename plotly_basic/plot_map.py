import os

import plotly
import plotly.plotly as py
import plotly.figure_factory as ff

import numpy as np
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

df_sample = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/laucnty16.csv')
df_sample['State FIPS Code'] = df_sample['State FIPS Code'].apply(lambda x: str(x).zfill(2))
df_sample['County FIPS Code'] = df_sample['County FIPS Code'].apply(lambda x: str(x).zfill(3))
df_sample['FIPS'] = df_sample['State FIPS Code'] + df_sample['County FIPS Code']

colorscale = ["#f7fbff", "#ebf3fb", "#deebf7", "#d2e3f3", "#c6dbef", "#b3d2e9", "#9ecae1",
              "#85bcdb", "#6baed6", "#57a0ce", "#4292c6", "#3082be", "#2171b5", "#1361a9",
              "#08519c", "#0b4083", "#08306b"]
endpts = list(np.linspace(1, 12, len(colorscale) - 1))
fips = df_sample['FIPS'].tolist()
values = [faker.random_int() for z in range(len(fips))]

fig = ff.create_choropleth(
    fips=fips, values=values,
    binning_endpoints=endpts,
    colorscale=colorscale,
    show_state_data=False,
    show_hover=True, centroid_marker={'opacity': 0},
    asp=2.9, title='Result Sheet',
    legend_title='Total Responses'
)
_path = os.path.join("/home/quixom/Desktop", 'temp.html')
plotly.offline.plot(fig, validate=False, filename=_path)
