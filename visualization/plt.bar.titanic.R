#!/usr/bin/env Rscript
df = data.frame(Titanic)

male_yes = sum(df[df$Sex == "Male" & df$Survived == "Yes", "Freq"])
male_no = sum(df[df$Sex == "Male" & df$Survived == "No", "Freq"])

female_yes = sum(df[df$Sex == "Female" & df$Survived == "Yes", "Freq"])
female_no = sum(df[df$Sex == "Female" & df$Survived == "No", "Freq"])

print(c(male_yes, male_no, female_yes, female_no)) # => 367, 1364, 344, 126
data = matrix(c(male_yes, male_no, female_yes, female_no), ncol=2)

# 簡易可視化
barplot(
  data,
  beside=T,
  legend.text=c("Yes", "No"),
  names.arg=c("Male", "Female"),
  col=c("red", "blue")
)
