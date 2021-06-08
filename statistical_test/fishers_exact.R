#!/usr/bin/env Rscript
# 男性_生存、男性_死亡、女性_生存、女性_死亡
data = matrix(c(367, 1364, 344, 126), ncol=2)

print(fisher.test(data)$p.value) # 2.690694e-96

# 参考値：カイ二乗検定
# chisq.test(data)$p.value # => 7.565462e-101
