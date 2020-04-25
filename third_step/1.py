import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


s = pd.Series([1,3,5,7,6,9])
print(s)

s.plot(grid=True)

plt.show()

# import os,ps
# ps.show(os.path.basename(__file__))
