from pyecharts.charts import Boxplot
import pyecharts.options as opts
import pandas as pd

df = pd.read_csv('city_day.csv')
data = df.loc[df['City'] == 'Delhi', ['Date', 'AQI']]

dom1, dom2, dom3 = [], [], []

list1 = []
for date, AQI in zip(data['Date'], data['AQI']):
    year = date.split('-')[0]
    if year in ['2015', '2016']:
        dom1.append(AQI)
    elif year in ['2017', '2018']:
        dom2.append(AQI)
    elif year in ['2019', '2020']:
        dom3.append(AQI)

x = ['2015-2016年', '2017-2018年', '2019-2020年']
y = [dom1, dom2, dom3]

boxplot = Boxplot()

boxplot.add_xaxis(x)
boxplot.add_yaxis('Delhi', boxplot.prepare_data(y))

boxplot.set_global_opts(
    title_opts=opts.TitleOpts(
        title='2015-2020印度德里AQI箱型图',
        pos_left='center',
    ),
    legend_opts=opts.LegendOpts(
        pos_left='left',
        orient='vertical',
    )
)

boxplot.render('boxplot_AQI.html')
