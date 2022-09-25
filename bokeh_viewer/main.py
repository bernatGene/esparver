import os
from functools import partial

import numpy as np
import copy
import xyzservices.providers as xyz

from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import column, row, grid, layout
from bokeh.tile_providers import get_provider
from bokeh.models import (
    ColumnDataSource,
    Slider,
    Button,
    RadioButtonGroup,
    Select,
    Div,
    Text,
    Paragraph,
    TextInput,
    Spinner,
    Toggle,
    expr,
)

from bokeh.events import MouseWheel


tile_provider = get_provider(xyz.OpenStreetMap.Mapnik)

# range bounds supplied in web mercator coordinates
p = figure(x_range=(-2000000, 6000000), y_range=(-1000000, 7000000),
           x_axis_type="mercator", y_axis_type="mercator", width=1200, height=720, active_scroll="wheel_zoom")
p.add_tile(tile_provider)

curdoc().add_root(p)