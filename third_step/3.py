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

dates =[d.strftime("%Y-%m-%d") for d in pd.date_range("20200425",periods=6)]

values=[
    [100,85],
    [90,20],
    [70,60],
    [100,30],
    [50,90],
    [99,100]
]

df = pd.DataFrame(values,index=dates,columns=list("AB"))
print(df)
ax= df.plot(kind="bar")
autolabel(ax)

plt.show()

# import os,ps
# ps.show(os.path.basename(__file__))





