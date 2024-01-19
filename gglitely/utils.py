from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.io as pio
import plotly.tools as tls
import matplotlib.pyplot as plt
from plotly.graph_objs._figure import Figure
import numpy as np


def litely(fig):
    plotly_fig = tls.mpl_to_plotly(fig)
    gglitely_fig = gglitely(data=plotly_fig.data, layout=plotly_fig.layout, frames=plotly_fig.frames)
    gglitely_fig.layout = None
    gglitely_fig.update_layout(template="plotly_white")
    gglitely_fig.update_layout(width=600, height=400)
    return gglitely_fig