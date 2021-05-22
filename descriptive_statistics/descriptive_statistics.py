import scipy
import statistics
import numpy as np
import pandas as pd
import scipy.stats as st

group1 = [0.7, -1.6, -0.2, -1.2, -0.1, 3.4, 3.7, 0.8, 0.0, 2.0]
group2 = [1.9, 0.8, 1.1, 0.1, -0.1, 4.4, 5.5, 1.6, 4.6, 3.4]

# 平均値
# => 0.75
print(np.mean(group1))
print(pd.Series(group1).mean())
print(scipy.mean(group1))
print(statistics.mean(group1))

# 中央値
# => 0.35
print(np.median(group1))
print(pd.Series(group1).median())
print(statistics.median(group1))

# 最小値
# => -1.6
print(np.min(group1))

# 最大値
# => 3.7
print(np.max(group1))

# 25%, 75%値
# => -0.175, 1.7
print(np.percentile(group1, 25))
print(np.percentile(group1, 75))

# 標準偏差（不偏分散平方根）
# => 1.7890096577591625
print(statistics.stdev(group1))
print(pd.Series(group1).std())

# 標本標準偏差
# => 1.6972035823671832
print(np.std(group1))

# 平均値の信頼区間
# => (-0.5297804134938644, 0.75, 2.0297804134938646)
def confidence_interval(a, percentile=0.95):
    arithmetic_mean = scipy.mean(a)
    ci_lower, ci_upper = st.t.interval(percentile, len(a)-1, loc=arithmetic_mean, scale=st.sem(a))
    return ci_lower, arithmetic_mean, ci_upper
print(confidence_interval(group1))
