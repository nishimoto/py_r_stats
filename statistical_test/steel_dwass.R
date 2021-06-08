#!/usr/bin/env Rscript
# install.packages("NSM3")
library("NSM3")

values = c(1, 2, 3, 5, 1, 12, 31, 54, 62, 12, 10, 12, 6, 74, 11)
groups = c(1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3)

# デフォルトではMonte Carloが使用される。
# 試行数が10,000未満の場合はExactと同じとなる。
# 再現性確保のためにseedを設定する
set.seed(0)
p_monte = pSDCFlig(values, groups)
print(p_monte$labels) # => "1 - 2" "1 - 3" "2 - 3"
print(p_monte$p.val)  # => 0.0090 0.0163 0.3780

# 近似法
p_asymptotic = pSDCFlig(values, groups, method="Asymptotic")
print(p_asymptotic$labels) # => "1 - 2" "1 - 3" "2 - 3"
print(p_asymptotic$p.val)  # => 0.02344837 0.02396820 0.35445269

# 正確法
set.seed(0)
p_exact = pSDCFlig(values, groups, method="Exact")
print(p_exact$labels) # => "1 - 2" "1 - 3" "2 - 3"
print(p_exact$p.val)  # => 0.008253651 0.015936445 0.375481661
