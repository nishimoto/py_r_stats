#!/usr/bin/env python
#!pip install japanize_matplotlib # プロット中で日本語を使用するためにインストール

import itertools
import pandas as pd
import matplotlib.pylab as plt
from IPython.display import display

df = pd.read_csv("mnist_train.csv", header=None, index_col=0)
display(df.head())

xs = []
ys = []
for x, y in itertools.permutations(range(28), 2):
    iloc = y * 28 + x
    if df.iloc[0, iloc] != 0:
        xs.append(x)
        ys.append(28 - y)
plt.scatter(xs, ys)
