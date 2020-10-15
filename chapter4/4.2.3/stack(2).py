from pyecharts.charts import Bar
import pyecharts.options as opts
import pandas as pd

pre_approval_rate = pd.read_csv('presidential_approval_rate.csv')
bar = Bar()

bar.add_xaxis(['支持', '反对', '不发表意见'])

for i in range(pre_approval_rate.iloc[:,0].size):
    issue = pre_approval_rate.loc[i, '政治举措']
    bar.add_yaxis(issue, [int(x) for x in pre_approval_rate.loc[i, ['支持', '反对', '不发表意见']]])

bar.set_global_opts(
    title_opts=opts.TitleOpts(
        title='柱状图数据堆叠示例',
        pos_left='center',
    ),
    legend_opts=opts.LegendOpts(
        pos_left='right',
        orient='vertical',
    ),
)
bar.set_series_opts(
    label_opts=opts.LabelOpts(
        is_show=False,
    ),
)

bar.render('stack(2).html')