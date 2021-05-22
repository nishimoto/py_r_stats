#!/usr/bin/env Rscript
# install.packages("effectsize")
library("effectsize")

group1 = c(0.7, -1.6, -0.2, -1.2, -0.1, 3.4, 3.7, 0.8, 0.0, 2.0)
group2 = c(1.9, 0.8, 1.1, 0.1, -0.1, 4.4, 5.5, 1.6, 4.6, 3.4)

d = cohens_d(group1, group2)$Cohens_d
d_low95 = cohens_d(group1, group2)$CI_low
d_high95 = cohens_d(group1, group2)$CI_high

g = hedges_g(group1, group2)$Hedges_g
g_low95 = hedges_g(group1, group2)$CI_low
g_high95 = hedges_g(group1, group2)$CI_high

print(d)        # => -0.8321811
print(d_low95)  # => -1.738817
print(d_high95) # => 0.09545044

print(g)        # => -0.7970185
print(g_low95)  # => -1.665346
print(g_high95) # => 0.09141732
