#!/usr/bin/env python
import scipy
import scipy.stats as st

group1 = [0.7, -1.6, -0.2, -1.2, -0.1, 3.4, 3.7, 0.8, 0.0, 2.0]
group2 = [1.9, 0.8, 1.1, 0.1, -0.1, 4.4, 5.5, 1.6, 4.6, 3.4]

p_value_pairedt = st.ttest_rel(group1, group2).pvalue
print(p_value_pairedt)  # => 0.00283289019738427
