import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

df = pd.read_csv("mnist_train.csv", header=None, index_col=0)
df_1000 = df.sample(1000)

# perplexityは30がデフォルトが多い（Rtsneもsklearnも30）
# 5〜50がよいと言われているため、5,30,50
colors = ["r", "g", "b", "c", "m", "y", "k", "orange", "pink", "gray"]
col = ["x", "y"]
for perplexity in [5, 30, 50]:
    model = TSNE(n_components=2, perplexity=perplexity, n_iter=500, verbose=3, random_state=1)
    transformed = model.fit_transform(df_1000)
    df_transformed = pd.DataFrame(transformed, index=df_1000.index, columns=col)
    df_transformed["color"] = [colors[i] for i in df_transformed.index]
    plt.scatter(df_transformed["x"], df_transformed["y"], c=df_transformed["color"])
    plt.savefig(f"scatter.tsne.{perplexity}.pdf")
    plt.clf()
