import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('fifa_data.csv')

left = data.loc[data['Preferred Foot'] == 'Left'].count()[0]
right = data.loc[data['Preferred Foot'] == 'Right'].count()[0]

plt.title('FIFA 2018 Pref. Foot Distribution', fontdict={'fontsize': 20, 'color': 'green'})

labels = ['Left', 'Right']
plt.pie([left, right], labels=labels, autopct='%.2f %%')

plt.savefig('fifa_foot.png')
plt.show()

