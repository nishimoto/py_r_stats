#!/usr/bin/env python
colors = ["r", "g", "b", "c", "m", "y", "k", "orange", "pink", "gray"]
pca = PCA(n_components=2, random_state=0)
df_pca = pd.DataFrame(pca.fit_transform(df_1000))
df_pca.columns = ["PC1", "PC2"]
df_pca["color"] = [colors[i] for i in df_1000.index]
