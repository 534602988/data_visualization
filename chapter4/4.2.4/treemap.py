import json
from pyecharts.charts import TreeMap
import pyecharts.options as opts

with open('GDP_data_1.json', 'r', encoding='utf-8') as f:
    j = json.load(f)
    data = [j]

map = TreeMap(
    init_opts=opts.InitOpts(width='1200px', height='800px')
)
map.add('',
        data,
        label_opts=opts.LabelOpts(position='inside'),
        )

map.render('map.html')
