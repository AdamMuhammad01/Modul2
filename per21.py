import plotly.graph_objects as go
import numpy as np


x = np.array([1,2,3,4,5])
y = np.array([2,1,4,1,3])

myFig = go.Figure(
    data = go.Bar(x=x, y=y)
)

myFig.show()