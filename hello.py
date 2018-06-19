import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy
import random

random_x = random.randint(1,10)
random_y = random.randint(1,10)

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers'
)

data = [trace]

# Plot and embed in ipython notebook!
py.iplot(data, filename='basic-scatter')

# or plot with: plot_url = py.plot(data, filename='basic-line')
