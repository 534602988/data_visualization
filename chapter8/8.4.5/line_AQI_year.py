from pyecharts.charts import Line
import pyecharts.options as opts
import pandas as pd


def get_line(city):

    data = df.loc[df['City'] == city, ['Date', 'AQI']]

    list1 = []
    for date in data['Date']:
        year = date.split('-')[0]
        list1.append(year)
    data['year'] = list1
    year_message = data.groupby(['year'])
    year_com = year_message['AQI'].agg(['mean'])
    year_com.reset_index(inplace=True)
    year_com_last = year_com.sort_index()

    y = [e for e in year_com_last['mean']]

    return y


df = pd.read_csv('city_day.csv')
cities = ['Ahmedabad', 'Chennai', 'Delhi', 'Lucknow']

line = Line()

line.add_xaxis(['2015', '2016', '2017', '2018', '2019', '2020'])
for city in cities:
    y = get_line(city)
    line.add_yaxis(city, y)

line.set_series_opts(
    label_opts=opts.LabelOpts(is_show=False),
)

line.set_global_opts(
    title_opts=opts.TitleOpts(
        title='2015-2020印度四大城市AQI年均走势图',
        pos_left='center',
    ),
    legend_opts=opts.LegendOpts(
        pos_left='left',
        orient='vertical',
    )
)

line.render('line_AQI.html')
