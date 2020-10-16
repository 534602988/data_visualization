import numpy as np
import math
from itertools import groupby
import pandas as pd

birth = pd.read_csv('birthrate.csv')
birth.dropna(subset=['2008'], inplace=True)

dirt = {}
data = list(round(birth['2008'], 1))
rangenum = []

for k,g in groupby(sorted(data), key=lambda x: int(x)):
    lst = map(str, list(map(lambda y: divmod(int(y*10), 10)[1], list(g))))
    dirt[k] = ' '.join(lst)
    rangenum.append(k)

num = list(range(rangenum[0], rangenum[-1], 2))

for i in num:
    a = ''
    for k in sorted(dirt.keys()):
        if 0 <= k-i <= 1:
            a = a + ' ' + dirt[k]
        elif k-i > 1:
            break
    print(str(i).rjust(5), '|', a)

