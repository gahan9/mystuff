import plotly
from plotly.graph_objs import *

mapbox_access_token = "pk.eyJ1IjoiZy1xdWl4b20iLCJhIjoiY2pmdGszNXBsM3NrYjM4bnZ4dWhwazh3ZSJ9.MckWPrzNYdWSG0e-xqzBqA"

data = Data([
    Scattermapbox(
        lat=['45.5017'],
        lon=['-73.5673'],
        mode='markers',
        marker=Marker(
            size=14
        ),
        text=['Montreal'],
    )
])

layout = Layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=45,
            lon=-73
        ),
        pitch=0,
        zoom=5
    ),
)

fig = dict(data=data, layout=layout)
plotly.offline.plot(fig, filename='Mapbox')

