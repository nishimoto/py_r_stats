#!/usr/bin/env Rscript
get_ncp_t <- function(t, df_error, conf.level = 0.95) {
  alpha <- 1 - conf.level
  probs <- c(alpha / 2, 1 - alpha / 2)
  
  ncp <- suppressWarnings(optim(
    par = 1.1 * rep(t, 2),
    fn = function(x) {
      p <- pt(q=t, df=df_error, ncp=x)
      abs(max(p) - probs[2]) + abs(min(p) - probs[1])
    },
    control = list(abstol = 1e-09)
  ))
  
  t_ncp <- unname(sort(ncp$par))
  return(t_ncp)
}

group1 = c(0.7, -1.6, -0.2, -1.2, -0.1, 3.4, 3.7, 0.8, 0.0, 2.0)
group2 = c(1.9, 0.8, 1.1, 0.1, -0.1, 4.4, 5.5, 1.6, 4.6, 3.4)

n1 = length(group1)
n2 = length(group2)
hn <- (1 / n1 + 1 / n2)

# 非心t分布の自由度
df = n1 + n2 - 2

# t検定における統計値（t値）を求める
t_test_result = t.test(group1, group2)
t = t_test_result$statistic

# 非心度を探索
t_lowhigh <- get_ncp_t(t, df, 0.95)

ci_low <- t_lowhigh[1] * sqrt(hn)
ci_high <- t_lowhigh[2] * sqrt(hn)

print(ci_low)  # => -1.738817
print(ci_high) # => 0.09545044
