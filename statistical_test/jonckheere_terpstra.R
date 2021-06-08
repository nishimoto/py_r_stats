#!/usr/bin/env Rscript
# データの生成
set.seed(1234)
g <- rep(1:5, rep(10,5))
x <- rnorm(50)
x[1:2] <- mean(x[1:2]) # tied data

# clinfun => タイ補正なし
# install.packages("clinfun")
library("clinfun")
jonckheere.test(x+0.3*g, g) # => 0.01741

# PMCMRplus => タイ補正あり
# install.packages("PMCMRplus")
library(PMCMRplus)
jonckheereTest(x+0.3*g, g) # => 0.0174
