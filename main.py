from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, Range1d, LabelSet, Label
import random
from bokeh.plotting import Figure
import numpy as np


plot=Figure()
source=ColumnDataSource(dict(x=[], y=[], avg=[]))
plot.scatter(x='x', y='y', size=8, source=source)
labels = LabelSet(x='x', y='y', text='avg', level='glyph',
              x_offset=5, y_offset=5, source=source, render_mode='canvas')
#fig.line(source=source, x='x', y = 'y', line_width=2, alpha=85, color='red')
#fig.line(source=source, x='x', y = 'avg', line_width=2, alpha=85, color='blue')
plot.add_layout(labels)
plot.toolbar.logo = None
plot.min_border_top = 0
plot.xgrid.grid_line_color = None
plot.ygrid.grid_line_color = "#999999"
plot.yaxis.axis_label = "Meters"
plot.ygrid.grid_line_alpha = 0.1
plot.xaxis.axis_label = "Meters"
plot.xaxis.major_label_orientation = 1
ct = 0
sine_sum=0


def update_data():
	global ct, sine_sum
	ct = random.uniform(1,10)
	sine =random.uniform(10,1)
	new_data= dict(x=[ct], y=[sine], avg=[sine/ct])
	print new_data
	source.stream(new_data, 50)

curdoc().add_root(plot)
curdoc().add_periodic_callback(update_data, 1000)

