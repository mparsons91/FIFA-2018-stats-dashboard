import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('fifa_data.csv')
data.Weight = [int(x.strip('lbs')) if type(x) == str else x for x in data.Weight]

plt.style.use('ggplot')
plt.title('FIFA 2018 Player Weight Distribution (lbs)')

light = data.loc[data.Weight < 125].count()[0]
light_medium = data.loc[(data.Weight >= 125) & (data.Weight < 150)].count()[0]
medium = data.loc[(data.Weight >= 150) & (data.Weight < 175)].count()[0]
medium_heavy = data.loc[(data.Weight >= 175) & (data.Weight < 200)].count()[0]
heavy = data.loc[data.Weight > 200].count()[0]

weights = [light, light_medium, medium, medium_heavy, heavy]
labels = ['Under 125', '125-150', '150-175', '175-200', 'Over 200']
explode = (.4, .1, 0, 0, .4)

plt.pie(weights, labels=labels, autopct='%.2f %%', pctdistance=0.8, explode=explode)

plt.savefig('player_weight.png')
plt.show()