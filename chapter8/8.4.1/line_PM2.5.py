from pyecharts.charts import Line
import pyecharts.options as opts
import pandas as pd

df = pd.read_csv('city_day.csv')
data = df.loc[df['City'] == 'Delhi', ['Date', 'PM2.5']]

x = [e for e in data['Date']]
y = [e for e in data['PM2.5']]

line = Line()
line.add_xaxis(x)
line.add_yaxis('Delhi', y)

line.set_series_opts(
    areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
    markpoint_opts=opts.MarkPointOpts(
        data=[
            opts.MarkPointItem(type_='max', name='最大值'),
            opts.MarkPointItem(type_='min', name='最小值'),
        ]
    ),
    markline_opts=opts.MarkLineOpts(
        data=[
            opts.MarkLineItem(type_='average'),
        ]
    ),
    label_opts=opts.LabelOpts(is_show=False),
)

line.set_global_opts(
    title_opts=opts.TitleOpts(
        title='2015-2020印度德里PM2.5走势图',
        pos_left='center',
    ),
    legend_opts=opts.LegendOpts(
        pos_left='left',
        orient='vertical',
    )
)

line.render('line_PM2.5.html')
