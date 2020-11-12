from pyecharts.charts import Pie
from pyecharts.charts import Grid
import pyecharts.options as opts
import pandas as pd


def get_pie(city, center1, center2):
    data = df.loc[df['City'] == city, ['Date', 'AQI_Bucket']]

    rank_message = data.groupby(['AQI_Bucket'])
    rank_com = rank_message['AQI_Bucket'].agg(['count'])
    rank_com.reset_index(inplace=True)
    rank_com_last = rank_com.sort_values('count', ascending=False)

    x = rank_com_last['AQI_Bucket']
    y = rank_com_last['count']

    pie = Pie(init_opts=opts.InitOpts(width='400px', height='300px'))

    input_data = [list(z) for z in zip(x, y)]
    pie.add(city, input_data, center=center1, radius=['15%', '30%'])

    pie.set_series_opts(
        label_opts=opts.LabelOpts(formatter='{b}：{d}%')
    )

    pie.set_global_opts(
        title_opts=opts.TitleOpts(
            title=city,
            pos_left=center2[0],
            pos_top=center2[1],
        ),
        legend_opts=opts.LegendOpts(
            is_show=False
        )
    )

    return pie


df = pd.read_csv('city_day.csv')
cities = ['Ahmedabad', 'Chennai', 'Delhi', 'Lucknow']
pos1 = [['25%', '25%'], ['25%', '75%'], ['75%', '25%'], ['75%', '75%']]
pos2 = [['20%', '23%'], ['22%', '74%'], ['73%', '23%'], ['71%', '74%']]

grid = Grid(init_opts=opts.InitOpts(width='1200px', height='800px'))
for i in range(len(cities)):
    grid.add(get_pie(cities[i], pos1[i], pos2[i]), grid_opts=opts.GridOpts())
grid.render('grid.html')
