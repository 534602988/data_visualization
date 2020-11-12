from pyecharts.charts import Calendar
import pyecharts.options as opts
import pandas as pd
import datetime

df = pd.read_csv('city_day.csv')
data = df.loc[df['City'] == 'Delhi', ['Date', 'PM2.5']]

list1 = []
for date, pm in zip(data['Date'], data['PM2.5']):
    time_list = date.split('-')
    time = datetime.date(int(time_list[0]), int(time_list[1]), int(time_list[2]))
    list1.append([str(time), pm])

calendar = Calendar()

calendar.add(
    '',
    list1,
    calendar_opts=opts.CalendarOpts(
        pos_top="120",
        pos_left="30",
        pos_right="30",
        range_="2017",
        yearlabel_opts=opts.CalendarYearLabelOpts(is_show=False),
        ),
    )

calendar.set_global_opts(
        title_opts=opts.TitleOpts(pos_top="30", pos_left="center", title="2017年印度德里空气质量情况"),
        visualmap_opts=opts.VisualMapOpts(
            max_=300, min_=0, orient="horizontal", is_piecewise=False
        ),
    )

calendar.render('heatmap.html')
