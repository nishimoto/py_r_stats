#!/usr/bin/env Rscript
# install.packages("Rtsne") # インストール
library("Rtsne")
set.seed(0)
setwd("/Users/nsmt/prv/hp/py_r_stats")

# input
df = read.csv("mnist_train.csv", header=FALSE)
df_1000 = df[1:1000, ]
vec_ans = df_1000$V1
df_1000 = df_1000[, colnames(df_1000) != "V1"]

# main
df_1000_tsne_pp5 = Rtsne(df_1000, perplexity=5)
df_1000_tsne_pp30 = Rtsne(df_1000, perplexity=30)
df_1000_tsne_pp50 = Rtsne(df_1000, perplexity=50)

# output
pdf("scatter.Rtsne.5.pdf")
plot(df_1000_tsne_pp5$Y, col=vec_ans)
dev.off()

pdf("scatter.Rtsne.30.pdf")
plot(df_1000_tsne_pp30$Y, col=vec_ans)
dev.off()

pdf("scatter.Rtsne.50.pdf")
plot(df_1000_tsne_pp50$Y, col=vec_ans)
dev.off()
