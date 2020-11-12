import pyecharts.options as opts
from pyecharts.charts import ThemeRiver
import csv


x_data = []
y_data = []

with open('data.csv', 'r') as f:
    r_csv = list(csv.reader(f))
    for row in r_csv[1:]:
        y_data.append([row[0], int(row[1]), row[2]])
        if row[2] not in x_data:
            x_data.append(row[2])

(
    ThemeRiver(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add(
        series_name=x_data,
        data=y_data,
        singleaxis_opts=opts.SingleAxisOpts(
            pos_top="50",
            pos_bottom="50",
            type_="time",
        ),
    )
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="line")
    )
    .render("theme_river.html")
)