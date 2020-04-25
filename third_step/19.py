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

dfSize = df.groupby(["Team"])["Rank"].size().rename("参加次数")
dfRank = df.copy()[df["Rank"]==1].groupby(["Team"])["Rank"].size().rename("获得第一名的次数")
print(df)
print(dfSize)
print(dfRank)
df =pd.merge(dfRank, dfSize, on='Team',how='right')

df=df.sort_values(by="获得第一名的次数",ascending = False)
print(df)

ax= df.plot(kind="bar")
ax.set_xlabel("团队")
ax.set_ylabel("分数")

autolabel(ax)
for v in ax.get_xticklabels():
    v.set_rotation(360)



plt.rcParams['font.sans-serif']=['SimHei']
plt.show()

# import os,ps
# ps.show(os.path.basename(__file__))





