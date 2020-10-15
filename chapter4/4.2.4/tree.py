import json
from pyecharts.charts import Tree
import pyecharts.options as opts

with open('GDP_data.json', 'r', encoding='utf-8') as f:
    j = json.load(f)
    data = [j]

tree = Tree(
    init_opts=opts.InitOpts(width='1500px', height='1200px')
)
tree.add('', data)

tree.render('tree.html')
