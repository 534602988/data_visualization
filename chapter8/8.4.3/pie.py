from pyecharts.charts import Pie
import pyecharts.options as opts
import pandas as pd

df = pd.read_csv('city_day.csv')
data = df.loc[df['City'] == 'Delhi', ['Date', 'AQI_Bucket']]

rank_message = data.groupby(['AQI_Bucket'])
rank_com = rank_message['AQI_Bucket'].agg(['count'])
rank_com.reset_index(inplace=True)
rank_com_last = rank_com.sort_values('count', ascending=False)

x = rank_com_last['AQI_Bucket']
y = rank_com_last['count']

pie = Pie()

input_data = [list(z) for z in zip(x, y)]
pie.add('Delhi', input_data, radius=['30%', '75%'])

pie.set_series_opts(
    label_opts=opts.LabelOpts(formatter='{b}：{d}%')
)

pie.set_global_opts(
    title_opts=opts.TitleOpts(
        title='2015-2020印度德里空气质量情况',
        pos_left='center',
    ),
    legend_opts=opts.LegendOpts(
        pos_left='left',
        orient='vertical',
    )
)

pie.render('pie.html')
