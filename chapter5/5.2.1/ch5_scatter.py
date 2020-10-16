import ggplot as gp
import pandas as pd
import numpy as np

crime = pd.read_csv('crimeRatesByState2005.csv')
print(gp.ggplot(gp.aes(x='murder', y='burglary'), data=crime)+gp.geom_point(color='red'))
