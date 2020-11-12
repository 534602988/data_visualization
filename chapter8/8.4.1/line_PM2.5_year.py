from pyecharts.charts import Line
import pyecharts.options as opts
import pandas as pd

df = pd.read_csv('city_day.csv')
data = df.loc[df['City'] == 'Delhi', ['Date', 'PM2.5']]

list1 = []
for date in data['Date']:
    year = date.split('-')[0]
    list1.append(year)
data['year'] = list1
year_message = data.groupby(['year'])
year_com = year_message['PM2.5'].agg(['mean'])
year_com.reset_index(inplace=True)
year_com_last = year_com.sort_index()

x = [e for e in year_com_last['year']]
y = [int(e) for e in year_com_last['mean']]

line = Line()
line.add_xaxis(x)
line.add_yaxis('Delhi', y)

line.set_series_opts(
    markpoint_opts=opts.MarkPointOpts(
        data=[
            opts.MarkPointItem(type_='max', name='最大值'),
            opts.MarkPointItem(type_='min', name='最小值'),
        ]
    ),
    label_opts=opts.LabelOpts(is_show=False),
)

line.set_global_opts(
    title_opts=opts.TitleOpts(
        title='2015-2020印度德里PM2.5年度走势图',
        pos_left='center',
    ),
    legend_opts=opts.LegendOpts(
        pos_left='left',
        orient='vertical',
    )
)

line.render('line_PM2.5_year.html')
