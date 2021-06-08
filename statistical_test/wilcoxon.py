#!/usr/bin/env python
# Scipyのバージョンが1.5.0より大きいかによって一部挙動が代わります。
# ここでは、現状のGoogleColabに従い、1.4.1版の結果を記載します。
import sys
import scipy
import scipy.stats as st
print(f"Python {sys.version}")      # 3.7.10
print(f"Scipy {scipy.__version__}") # 1.4.1

group1 = [0.7, -1.6, -0.2, -1.2, -0.1, 3.4, 3.7, 0.8, 0.0, 2.0]
group2 = [1.9, 0.8, 1.1, 0.1, -0.1, 4.4, 5.5, 1.6, 4.6, 3.4]

p_value_wilc = st.wilcoxon(group1, group2, alternative="two-sided").pvalue
print(p_value_wilc)  # => 0.007632441648205508
