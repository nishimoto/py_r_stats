#!/usr/bin/env python
import scipy.stats as st # scipy version 1.3.1

data = [[367, 1364], [344, 126]]
print(st.fisher_exact(data)[1]) # => 2.6906937468576903e-96

# 参考値：カイ二乗検定
# st.chi2_contingency(data)[1] # => 7.565461964935766e-101
