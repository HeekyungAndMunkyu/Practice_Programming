weka = read.csv("cs-training_weka_998.csv", header = TRUE)
str(weka)
weka = weka[with(weka, order(weka$RevolvingUtilizationOfUnsecuredLines)), ]
head(weka)
p = 119520*0.80
weka = weka[1:p,]
write.csv(weka, "cs-training_weka_998.csv", row.names = FALSE)

weka = weka[with(weka, order(weka$NumberOfTime30.59DaysPastDueNotWorse)), ]
head(weka)

weka = weka[with(weka, order(weka$DebtRatio)), ]


weka = weka[with(weka, order(weka$MonthlyIncome)), ]


