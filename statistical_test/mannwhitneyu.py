#!/usr/bin/env python
import sys
import scipy
import scipy.stats as st
print(f"Scipy {scipy.__version__}")
# => 1.4.1

group1 = [0.7, -1.6, -0.2, -1.2, -0.1, 3.4, 3.7, 0.8, 0.0, 2.0]
group2 = [1.9, 0.8, 1.1, 0.1, -0.1, 4.4, 5.5, 1.6, 4.6, 3.4]

p_value_manh = st.mannwhitneyu(group1, group2, alternative="two-sided").pvalue
print(p_value_manh)  # => 0.06932757543362658
