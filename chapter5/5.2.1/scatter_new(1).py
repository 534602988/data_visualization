import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

crime = pd.read_csv('crimeRatesByState2005.csv')
# 去除全美平均值和华盛顿特区两个数据点
crime2 = crime[crime.state != 'United States']
crime2 = crime2[crime.state != 'District of Columbia']

x = list(crime2['murder'])
y = list(crime2['burglary'])

plt.figure()  # 创建一个图像

plt.scatter(x, y, s=50, c='r', marker='o', alpha=0.5)

poly = np.polyfit(x, y, deg=1)
py = np.polyval(poly, x)
py1 = py + 200
py2 = py - 200
plt.plot(x, py)
plt.plot(x, py1, alpha=0)
plt.plot(x, py2, alpha=0)
plt.fill_between(x, py1, py2, where=py1>py2, facecolor='red', alpha=0.2)

plt.grid(ls='--',c='black') # 添加参考线

# 设置x，y轴标签
font = {
    "family":"Microsoft YaHei"
}  # 设置字体
plt.xlabel('谋杀案', font)
plt.ylabel('入室盗窃案', font)

plt.show()
