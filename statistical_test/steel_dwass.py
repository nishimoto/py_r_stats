#!/usr/bin/env python
#! pip install scikit-posthocs
import pandas as pd
import scikit_posthocs as sp

x = pd.DataFrame({"a": [1, 2, 3, 5, 1], "b": [12, 31, 54, 62, 12], "c": [10, 12, 6, 74, 11]})
x = x.melt(var_name='groups', value_name='values')
print(x)
sp.posthoc_dscf(x, val_col='values', group_col='groups')
