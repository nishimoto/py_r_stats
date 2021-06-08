#!/usr/bin/env python
import scipy
import scipy.stats as st

data = [[4, 14], [3, 1]]
p_value_chisq = st.chi2_contingency(data)[1]

print(p_value_chisq) # => 0.1452510053118262
