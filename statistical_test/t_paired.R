#!/usr/bin/env Rscript
group1 = c(0.7, -1.6, -0.2, -1.2, -0.1, 3.4, 3.7, 0.8, 0.0, 2.0)
group2 = c(1.9, 0.8, 1.1, 0.1, -0.1, 4.4, 5.5, 1.6, 4.6, 3.4)
p_value_pairedt = t.test(x, y, paired=T)$p.value 
print(p_value_pairedt) # => 0.00283289
