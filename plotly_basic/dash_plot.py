import os

import plotly
import plotly.graph_objs as go
from faker import Faker

f = Faker()

_x = [f.name() for i in range(50)]
_y = [f.random_int() for i in range(50)]

data = [go.Scatter(x=_x, y=_y)]
_path = os.path.join("/home/quixom/Desktop", 'temp.html')
plotly.offline.plot(data, filename=_path)
