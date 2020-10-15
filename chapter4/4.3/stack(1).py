from pyecharts.charts import Line
import pyecharts.options as opts
import pandas as pd

year_poputation_age = pd.read_csv('us_population_by_age.csv')

x = [str(x) for x in year_poputation_age['year']]
y1 = [float(x) for x in year_poputation_age['year_under5']]
y2 = [float(x) for x in year_poputation_age['year5_19']]
y3 = [float(x) for x in year_poputation_age['year20_44']]
y4 = [float(x) for x in year_poputation_age['year45_64']]
y5 = [float(x) for x in year_poputation_age['year65above']]

line = Line(
    init_opts=opts.InitOpts(
        width='500px',
        height='500px',
    ),
)
line.add_xaxis(x)
line.add_yaxis('5岁以下', y1, is_smooth=True, stack=1)
line.add_yaxis('5至19岁', y2, is_smooth=True, stack=1)
line.add_yaxis('20至44岁', y3, is_smooth=True, stack=1)
line.add_yaxis('45至64岁', y4, is_smooth=True, stack=1)
line.add_yaxis('65岁以上', y5, is_smooth=True, stack=1)

line.set_global_opts(
    title_opts=opts.TitleOpts(title='人口老龄化'),
    yaxis_opts=opts.AxisOpts(
        splitline_opts=opts.SplitLineOpts(is_show=True),
    ),
    legend_opts=opts.LegendOpts(
        pos_left='right',
        orient='vertical',
    )
)
line.set_series_opts(
    areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
    label_opts=opts.LabelOpts(
        is_show=False,
    ),
)

line.render('stack(1).html')
