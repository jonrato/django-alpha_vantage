from django.shortcuts import render
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import pandas as pd
from math import pi
import datetime
from .utils import get_data, convert_to_df


def homepage(request):
    
    #We use get_data method from utils

    result = get_data('EUR','USD', 'Your API')

    source = convert_to_df(result)

    increasing = source.close > source.open
    decreasing = source.open > source.close
    w = 12*60*60*1000
    print(source)
    TOOLS = "pan, wheel_zoom, box_zoom, reset, save"

    title = 'EUR to USD chart'

    p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=700, plot_height=500, title = title)
    p.xaxis.major_label_orientation = pi / 4
    
    p.grid.grid_line_alpha = 0.3
    
    p.segment(source.date, source.high, source.date, source.low, color="black")
    p.vbar(source.date[increasing], w, source.open[increasing], source.close[increasing],
        fill_color="#D5E1DD", line_color="black"
    )
    p.vbar(source.date[decreasing], w, source.open[decreasing], source.close[decreasing], 
        fill_color="#F2583E", line_color="black"
    )

    script, div = components(p)

    return render(request,'pages/base.html',{'script':script, 'div':div })