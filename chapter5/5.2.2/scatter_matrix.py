import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

crime = pd.read_csv('crimeRatesByState2005.csv')

crime2 = crime[crime.state != 'United States']
crime2 = crime2[crime.state != 'District of Columbia']

crime2 = crime2.drop({'state'}, axis=1)
q = sns.pairplot(crime2, diag_kind='kde')

plt.show()
