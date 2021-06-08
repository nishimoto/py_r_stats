#!/usr/bin/env Rscript
df_1000_pca = prcomp(df_1000)
pdf("scatter.RPCA.pdf")
plot(df_1000_pca$x, col=vec_ans)
text(df_1000_pca$x[, 1], df_1000_pca$x[, 2], vec_ans)
dev.off()
