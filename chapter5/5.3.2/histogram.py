import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
titanic = pd.read_csv('birthrate.csv')
titanic.dropna(subset=['2008'], inplace=True)

plt.style.use('ggplot')
plt.hist(titanic['2008'], bins=10, color='steelblue', edgecolor='k', label='直方图')
plt.tick_params(top='off', right='off')
plt.xlabel('出生率(‰)')
plt.ylabel('频率(‰)')
plt.legend()
plt.show()
