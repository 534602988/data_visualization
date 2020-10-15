from pyecharts.charts import Pie
import pyecharts.options as opts
import pandas as pd

vote_result = pd.read_csv('vote_result.csv')
'''
Pie要求输入的数据格式为
[
[name1, value1],
[name2, value2],
[name3, value3],
...
]
故需要转换格式
'''
data = [list(z) for z in zip(vote_result['感兴趣的领域'], vote_result['票数'])]

pie = Pie()
pie.add('', data, center=['60%', '60%'], radius=['30%', '75%'])

pie.set_global_opts(
    title_opts=opts.TitleOpts(title='数据可视化-用户感兴趣领域',
                              subtitle='以下是读者的投票结果。\n'
                              '读者对金融医疗、医疗保健、市场业3个领域最感兴趣。'
                              ),
    legend_opts=opts.LegendOpts(pos_left='right',
                                orient='vertical',
                                ),
)
pie.set_series_opts(
    label_opts=opts.LabelOpts(formatter='{b}：{d}%'),
)
pie.render('ring.html')
