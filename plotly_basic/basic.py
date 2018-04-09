import plotly
from plotly.graph_objs import *
import datetime
import numpy


class BasicPlotting(object):
    def __init__(self, *args, **kwargs):
        self.x = kwargs.get('x', numpy.random.randn(2000))
        self.y = kwargs.get('y', numpy.random.randn(2000))
        self.mode = kwargs.get('mode', 'offline')
        self.graph_type = kwargs.get('graph_type', 'histogram')
        self.filename = kwargs.get('filename', self._generate_timestamp())
        self.title = "Default Title"

    @staticmethod
    def _generate_timestamp():
        return datetime.datetime.now().strftime('%Y-%d-%m_%H.%M')

    def setup_data(self, x=None, y=None, graph_type=None):
        x = x if x else self.x
        y = y if y else self.y
        graph_type = graph_type.lower() if graph_type else self.graph_type.lower()
        if graph_type == "histogram":
            return [Histogram2dContour(x=x, y=y, contours=Contours(coloring='heatmap')),
                    Scatter(x=x, y=y, mode='markers', marker=Marker(color='white', size=3, opacity=0.3))]
        else:
            return [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])]

    @staticmethod
    def cufflinks_plot():
        import cufflinks as cf
        plotly.offline.plot(cf.datagen.lines().iplot(asFigure=True,
                                                     kind='scatter', xTitle='Dates', yTitle='Returns', title='Returns'))

    def plot(self, title=None, filename=None, data=None):
        title = title if title else self.title
        filename = filename if filename else self.filename
        if self.mode == "offline":
            plotly.offline.plot(
                {
                    "data"  : self.setup_data(graph_type="histogram"),
                    "layout": Layout(title=title),
                },
                filename="{}.html".format(filename),
            )


if __name__ == "__main__":
    plot_obj = BasicPlotting(mode="offline", graph_type="histogram")
    # plot_obj.plot(title="histogram plot")
    plot_obj.cufflinks_plot()
