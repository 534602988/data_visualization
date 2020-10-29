import matplotlib.pyplot as plt
import pandas as pd

crime = pd.read_csv('crimeRatesByState2005.csv')

data_x = list(crime['murder'])
data_y = list(crime['burglary'])

plt.scatter(data_x, data_y, s=50, c='r', marker='o', alpha=0.5)

plt.grid(ls='--',c='black') # 添加参考线

# 设置x，y轴标签
font = {
    "family":"Microsoft YaHei"
}  # 设置字体
plt.xlabel('谋杀案', font)
plt.ylabel('入室盗窃案', font)

plt.show()
