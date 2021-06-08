#!/usr/bin/env Rscript
p_values = c(0.21, 0.001, 0.1, 0.06, 0.005)
print(p.adjust(p_values, method="bonferroni")) # => c(1.000, 0.005, 0.500, 0.300, 0.025)
