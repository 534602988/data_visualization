from pyecharts.charts import Bar
import pyecharts.options as opts
import pandas as pd

pre_approval_rate = pd.read_csv('presidential_approval_rate.csv')
bar = Bar()

bar.add_xaxis([str(x) for x in pre_approval_rate['政治举措']])
bar.add_yaxis('支持', [int(x) for x in pre_approval_rate['支持']], stack=1)
bar.add_yaxis('反对', [int(x) for x in pre_approval_rate['反对']], stack=1)
bar.add_yaxis('不发表意见', [int(x) for x in pre_approval_rate['不发表意见']], stack=1)

bar.set_global_opts(
    title_opts=opts.TitleOpts(
        title='柱状图数据堆叠示例',
    ),
    xaxis_opts=opts.AxisOpts(
        axislabel_opts=
        {
            "rotate": 30,
        },
    ),
)
bar.set_series_opts(
    label_opts=opts.LabelOpts(
        is_show=False,
    ),
)

bar.render('stack.html')
