import pandas as pd
import numpy as np
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import math

# 为了打印值，在series上
def autolabel(ax):
    
    for rect in ax.patches:
        x = rect.get_x() + rect.get_width()/2

        height = rect.get_height()
        height = height if math.isnan(height) ==False else 0
        ax.text(x=x, y=height, s=f"{int(height)}")

values = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}



df = pd.DataFrame(values)

df = df.groupby(["Team"])["Points"].sum().sort_values(ascending=False)
print(type(df))
print(df)
ax= df.plot(kind="bar")
autolabel(ax)
for v in ax.get_xticklabels():
    v.set_rotation(360)



plt.show()

# import os,ps
# ps.show(os.path.basename(__file__))





