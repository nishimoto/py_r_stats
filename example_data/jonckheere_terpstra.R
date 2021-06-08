#!/usr/bin/env Rscript
set.seed(1234)
g <- rep(1:5, rep(10,5))
x <- rnorm(50)
jonckheere.test(x+0.3*g, g)
x[1:2] <- mean(x[1:2]) # tied data

# ggplotで可視化
library(ggplot2)
df = data.frame(
  x=as.factor(g),
  y=x+0.3*g
)
ggplot(data=df, aes(group=x, y=y, fill=x)) + geom_boxplot()
