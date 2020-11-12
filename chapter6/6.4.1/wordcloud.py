from pyecharts.charts import WordCloud
import pyecharts.options as opts
import pandas as pd

post_data = pd.read_csv('post_data.csv')
post_data2 = post_data.groupby(by=['category']).agg({'views':sum}).reset_index()

data = [list(e) for e in zip(post_data2['category'], [str(e) for e in post_data2['views']])]

wordcloud = WordCloud()
wordcloud.add(series_name='', data_pair=data, word_size_range=[20, 100])

wordcloud.render('wordcloud.html')
