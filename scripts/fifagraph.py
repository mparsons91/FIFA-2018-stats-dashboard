import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fifa = pd.read_csv('fifa_data.csv')

#   Histogram
#   ______________________________________________________

bins = [40, 50, 60, 70, 80, 90, 100]
plt.hist(fifa.Overall, bins=bins)
plt.xticks(bins)
plt.ylabel('Number of Players')
plt.xlabel('Skill Level')
plt.title('Distribution of Player Skills in FIFA 2018')

plt.savefig('fifa_overall.png')

plt.show()