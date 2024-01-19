from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.io as pio
import plotly.tools as tls
import matplotlib.pyplot as plt
from plotly.graph_objs._figure import Figure
import numpy as np


class gglitely(Figure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update_layout(template="plotly_white")
        self.update_layout(width=600, height=400)
    def __add__(self,geom):
        temp = gglitely(data=self.data, layout=self.layout, frames=self.frames)
        temp.add_trace(geom)
        return temp
    def resize(self,width=600,height=400):
        self.update_layout(width=width, height=height)
        return self
        
class point(go.Scatter):
    def __init__(self, *args, **kwargs):       
        color = kwargs.pop('colour', kwargs.pop('col', kwargs.pop('color', None)))

        symbol = kwargs.pop('symbol',kwargs.pop('pch', kwargs.pop('shape', 'circle')))
        pch_mapping = {
            0: 'square-open',
            1: 'circle-open',
            2: 'triangle-up-open',
            3: 'cross-open',
            4: 'x-open',
            5: 'diamond-open',
            6: 'triangle-down-open',
            7: 'cross',
            8: 'x',
            9: 'diamond-tall-open',
            10: 'circle',
            11: 'diamond-tall',
            12: 'square',
            13: 'cross-thin-open',
            14: 'diamond-open',
            15: 'square',
            16: 'circle',
            17: 'triangle-up',
            18: 'triangle-down',
            19: 'circle',
            20: 'circle',
            21: 'circle',
            22: 'square',
            23: 'diamond-tall',
            24: 'triangle-up',
            25: 'triangle-down',
        }
        if isinstance(symbol,int):
            symbol = pch_mapping[symbol]

        opacity = kwargs.pop('opacity', kwargs.pop('alpha', 1))
        if isinstance(opacity, list) or (isinstance(opacity, np.ndarray) and opacity.ndim == 1):
            opacity = np.array(opacity) / np.array(opacity).max()
            
        size = kwargs.pop('cex', kwargs.pop('size', None))            
        fillcolor = kwargs.pop('fill', None)             
        line = kwargs.pop('stroke', None)
        marker = dict(
            size=size,
            color=color,
            opacity=opacity,
            line=line,
            symbol=symbol
        )
        if fillcolor:
            marker['fillcolor'] = fillcolor
        kwargs['marker'] = marker
        super().__init__(mode='markers', *args, **kwargs)
class line(go.Scatter):
    def __init__(self, *args, **kwargs):
        color = kwargs.pop('colour', kwargs.pop('col', kwargs.pop('color', None)))
        
        dash = kwargs.pop('lty', kwargs.pop('linetype', kwargs.pop('dash', None)))
        lty_mapping = {
            0: None,                # 'blank' - no line
            1: 'solid',             # 'solid' - solid line
            2: '8px,3px,8px,3px',   # 'dashed' - dashed line
            3: 'dot',               # 'dotted' - dotted line
            4: 'dashdot',           # 'dotdash' - dash-dot line
            5: 'longdash',          # 'longdash' - long dashed line
            6: 'longdashdot',       # 'twodash' - two dash line (not directly equivalent in Plotly, but 'longdashdot' is close)
        }
        if isinstance(dash,int):
            dash = lty_mapping[dash]        
        
        width = kwargs.pop('lwd', kwargs.pop('linewidth', kwargs.pop('width', None)))
        opacity = kwargs.pop('alpha', kwargs.pop('opacity', 1))
        kwargs['line'] = dict(color=color, width=width, dash=dash)
        kwargs['opacity'] = opacity
        super().__init__(mode='lines', *args, **kwargs)