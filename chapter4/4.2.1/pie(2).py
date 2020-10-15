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
pie.add('', data)

pie.set_global_opts(
    title_opts=opts.TitleOpts(title='饼图示例',
                              pos_left='center',  # 以最左为基准设置title的位置
                              ),
    legend_opts=opts.LegendOpts(orient='vertical',
                                pos_left='left',  # 以最左为基准设置legend的位置
                              ),
)
pie.set_series_opts(
    label_opts=opts.LabelOpts(formatter='{b}：{d}%')
)
pie.render('pie(2).html')
