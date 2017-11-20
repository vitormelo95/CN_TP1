import plotly.plotly as py
import plotly.graph_objs as go

class PlotStat(object):
    def __init__(self, stat_list):
        self.data = stat_list

    trace_high = go.Scatter(
                    x=df.Date,
                    y=df['AAPL.High'],
                    name = "AAPL High",
                    line = dict(color = '#17BECF'),
                    opacity = 0.8)

    trace_low = go.Scatter(
                    x=df.Date,
                    y=df['AAPL.Low'],
                    name = "AAPL Low",
                    line = dict(color = '#7F7F7F'),
                    opacity = 0.8)

    data = [trace_high,trace_low]

    layout = dict(
        title = "Manually Set Date Range",
        xaxis = dict(
            range = ['2016-07-01','2016-12-31'])
    )

    fig = dict(data=data, layout=layout)
    py.iplot(fig, filename = "Manually Set Range")
