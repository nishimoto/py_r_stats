#!/usr/bin/env Rscript
# 男性_生存、男性_死亡、女性_生存、女性_死亡
data = matrix(c(4, 14, 3, 1), ncol=2)

p_value_chisq = chisq.test(data)$p.value
print(p_value_chisq) # => 0.145251
