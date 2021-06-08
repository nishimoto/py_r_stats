#!pip install japanize_matplotlib # プロット中で日本語を使用するためにインストール
import pandas as pd
import seaborn as sns
import japanize_matplotlib
import matplotlib.pyplot as plt
from IPython.display import display

df = pd.DataFrame({
  "国語": [55, 28, 48, 49, 66, 49, 45, 36, 64, 34],
  "社会": [83, 42, 68, 77, 67, 71, 61, 51, 78, 68],
  "数学": [19, 29, 8, 10, 25, 17, 18, 35, 19, 22],
  "理科": [51, 52, 33, 45, 46, 39, 36, 52, 33, 60],
  "英語": [94, 66, 64, 81, 92, 78, 68, 77, 84, 82]  
}, index=["A01", "A02", "A03", "A04", "A05", "A06", "A07", "A08", "A09", "A10"])
display(df.corr()) # => 相関係数（ピアソン）行列をtableとして出力
sns.pairplot(df)
plt.savefig("pairplot.png")
