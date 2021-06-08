#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Jupyter上で確認したい場合は必要
# %matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

df = pd.DataFrame({
  "国語": [55, 28, 48, 49, 66, 49, 45, 36, 64, 34],
  "社会": [83, 42, 68, 77, 67, 71, 61, 51, 78, 68],
  "数学": [19, 29, 8, 10, 25, 17, 18, 35, 19, 22],
  "理科": [51, 52, 33, 45, 46, 39, 36, 52, 33, 60],
  "英語": [94, 66, 64, 81, 92, 78, 68, 77, 84, 82]
}, index=["A01", "A02", "A03", "A04", "A05", "A06", "A07", "A08", "A09", "A10"])

pca = PCA(n_components=2, random_state=0)
df_pca = pd.DataFrame(pca.fit_transform(df))
df_pca.columns = ["PC1", "PC2"]

# 寄与率の表示
pc1_explained_variance_ratio = 100 * pca.explained_variance_ratio_[0]
pc2_explained_variance_ratio = 100 * pca.explained_variance_ratio_[1]

# パーセント表示に変更、小数点1桁まで表示
pc1_explained_variance_ratio = format(pc1_explained_variance_ratio, '.1f')
pc2_explained_variance_ratio = format(pc2_explained_variance_ratio, '.1f')

# 観測変数の寄与度
df_components = pd.DataFrame(pca.components_).T
df_components.index = df.columns
df_components.columns = ["PC1", "PC2"]

# 描画
# メイン
plt.scatter(df_pca["PC1"], df_pca["PC2"])

# 観測変数の寄与度
# Rっぽく
for x, y, text in zip(df_components["PC1"], df_components["PC2"], df_components.index):
    plt.arrow(0, 0, x, y, color="red", width=0.025)
    plt.text(x, y, text)
plt.xlabel(f"PC1({pc1_explained_variance_ratio}%)")
plt.ylabel(f"PC2({pc2_explained_variance_ratio}%)")
plt.savefig("plt.pca.midterm_test.sklearn.png")
