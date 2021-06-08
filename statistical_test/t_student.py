#!/usr/bin/env python
import sys
import scipy
import scipy.stats as st

group1 = [0.7, -1.6, -0.2, -1.2, -0.1, 3.4, 3.7, 0.8, 0.0, 2.0]
group2 = [1.9, 0.8, 1.1, 0.1, -0.1, 4.4, 5.5, 1.6, 4.6, 3.4]

p_value_studentt = st.ttest_ind(group1, group2, euqal_var=True).pvalue
print(p_value_studentt)  # => 0.07918671421593818
