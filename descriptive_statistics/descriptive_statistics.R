#!/usr/bin/env Rscript
group1 <- c(0.7, -1.6, -0.2, -1.2, -0.1, 3.4, 3.7, 0.8, 0.0, 2.0)
group2 <- c(1.9, 0.8, 1.1, 0.1, -0.1, 4.4, 5.5, 1.6, 4.6, 3.4)

# 平均値: 0.75
print(mean(group1))

# 中央値: 0.52
print(median(group1))

# 最小値: -1.04
print(min(group1))

# 最大値: 1.81
print(max(group1))

# 25%, 75%値: -0.175, 1.7
print(quantile(group1, 0.25))
print(quantile(group1, 0.75))

# 標準偏差（不偏分散平方根）: 1.78901
sd(group1)

# (95%)信頼区間: -0.5297804  0.7500000  2.0297804
confidence_interval <- function(x, percentile=0.95) {
  result_t_test = t.test(x, conf.level=percentile)
  return(c(result_t_test[[4]][1], mean(x), result_t_test[[4]][2]))
}
print(confidence_interval(group1))
