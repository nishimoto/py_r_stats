#!/usr/bin/env python
import scipy.stats as st # scipy version 1.3.1

data = [[4, 14], [3, 1]] # Titanicデータを100分の1
print(st.fisher_exact(data)[1]) # => 0.07655502392344488
print(st.chi2_contingency(data)[1]) # => 0.1452510053118262
