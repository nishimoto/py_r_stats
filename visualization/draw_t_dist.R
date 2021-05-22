#!/usr/bin/env Rscript
curve(dt(x, df=18, ncp=0.2134337), -8, 4)
curve(dt(x, df=18, ncp=-3.8881125), -8, 4, add=T)
abline(v=t)
print(qt(0.025, df=18, ncp=0.2134337))  # => -1.860813
print(qt(0.975, df=18, ncp=-3.8881125)) # => -1.860813
