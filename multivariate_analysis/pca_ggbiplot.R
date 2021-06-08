#!/usr/bin/env Rscript
# 初回のみ
# install.packages("devtools")
# devtools::install_github("vqv/ggbiplot")

library("ggbiplot")

国語 = c(55, 28, 48, 49, 66, 49, 45, 36, 64, 34)
社会 = c(83, 42, 68, 77, 67, 71, 61, 51, 78, 68)
数学 = c(19, 29, 8, 10, 25, 17, 18, 35, 19, 22)
理科 = c(51, 52, 33, 45, 46, 39, 36, 52, 33, 60)
英語 = c(94, 66, 64, 81, 92, 78, 68, 77, 84, 82)

df = data.frame(
  国語=国語,
  社会=社会,
  数学=数学,
  理科=理科,
  英語=英語
)

rownames(df) = c("A01", "A02", "A03", "A04", "A05", "A06", "A07", "A08", "A09", "A10")
ggbiplot(prcomp(df)) # groupsで簡易に色分けができる
