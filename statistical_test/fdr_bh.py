#!/usr/bin/env python
from statsmodels.stats.multitest import multipletests

p_values = [0.21, 0.001, 0.1, 0.06, 0.005]
print(multipletests(p_values, method='fdr_bh')[1]) # => [0.21, 0.005, 0.125, 0.1, 0.0125]
