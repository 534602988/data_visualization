import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
titanic = pd.read_csv('birthrate.csv')
titanic.dropna(subset=['2008'], inplace=True)

plt.style.use('ggplot')
plt.hist(
    titanic['2008'],
    bins=np.arange(
        titanic['2008'].min(),
        titanic['2008'].max(),
        3
    ),
    normed=True,
    color='steelblue',
    edgecolor='k'
)
plt.title('2008出生直方图和密度图')
plt.xlabel('出生率(‰)')
plt.ylabel('频率(‰)')
kde = mlab.GaussianKDE(titanic['2008'])
x2 = np.linspace(titanic['2008'].min(), titanic['2008'].max(), 1000)
line2 = plt.plot(x2, kde(x2), 'g-', linewidth=2)
plt.tick_params(top='off', right='off')
plt.show()
