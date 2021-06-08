#!/usr/bin/env python
import pandas as pd
import matplotlib.pylab as plt

df = pd.DataFrame({
    "a": [1, 2, 3, 5, 1],
    "b": [12, 31, 54, 62, 12],
    "c": [10, 12, 6, 74, 11]
})

df.plot(kind="box")
plt.savefig("boxplot.steel-dwass.png")
