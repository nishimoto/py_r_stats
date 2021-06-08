#!/usr/bin/env Rscript
p_values = c(0.21, 0.001, 0.1, 0.06, 0.005)
p.adjust(p_values, method="fdr") # => c(0.2100, 0.0050, 0.1250, 0.1000, 0.0125)
