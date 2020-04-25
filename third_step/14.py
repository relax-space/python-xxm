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
        ax.text(x=x, y=height, s=f"{round(height,2)}")

dates =[d.strftime("%Y-%m-%d") for d in pd.date_range("20200425",periods=6)]

values={
    "A":[100,90,70,100,50,99],
    "B":[85,20,60,30,90,100],
}

df = pd.DataFrame(values,index=dates)
rowCount = df.shape[0]
dfA = df["A"].sort_values()[1:rowCount-1].mean()
dfB = df["B"].sort_values()[1:rowCount-1].mean()

index =[f"[{min(dates)} ~ {max(dates)}]"]
df =pd.DataFrame({
    "A":dfA,
    "B":dfB,
},index)
print(df)
ax= df.plot(kind="bar")
autolabel(ax)

for v in ax.get_xticklabels():
    v.set_rotation(350)

plt.show()

# import os,ps
# ps.show(os.path.basename(__file__))





