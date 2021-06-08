import pandas as pd
import matplotlib.pylab as plt

group1 = [0.7, -1.6, -0.2, -1.2, -0.1, 3.4, 3.7, 0.8, 0.0, 2.0]
group2 = [1.9, 0.8, 1.1, 0.1, -0.1, 4.4, 5.5, 1.6, 4.6, 3.4]

df = pd.DataFrame({
    "group1": group1,
    "group2": group2
})

# 棒グラフ（対応がある場合はこの可視化）
df.plot(kind="bar")
plt.savefig("plt.bar.sleep.png")

# 箱ひげ図（対応がない場合はこの可視化）
df.plot(kind="box", widths=0.66)
plt.savefig("plt.box.sleep.png")
