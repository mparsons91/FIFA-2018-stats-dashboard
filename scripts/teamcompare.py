import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('fifa_data.csv')
plt.title('FIFA 2018 Football Team Comparison')
plt.ylabel('FIFA Overall Rating')

barcelona = data.loc[data.Club == 'FC Barcelona']['Overall']
madrid = data.loc[data.Club == 'Real Madrid']['Overall']
revs = data.loc[data.Club == 'New England Revolution']['Overall']

labels = ['FC Barcelona', 'Real Madrid', 'NE Revolution']

boxes = plt.boxplot([barcelona, madrid, revs], labels=labels, patch_artist=True,
                    medianprops={'linewidth': 2})

for box in boxes['boxes']:
    box.set(color='#4286f4', linewidth=2)
    box.set(facecolor='#e0e0e0')

plt.savefig('team_compare.png')
plt.show()
