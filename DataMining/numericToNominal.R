wekatrain = read.csv("~/Practice_Python/DataScience/CreditScoring/training_balanced.csv", header = TRUE)

wekatrain$SeriousDlqin2yrs[wekatrain$SeriousDlqin2yrs == 0] = "n"
wekatrain$SeriousDlqin2yrs[wekatrain$SeriousDlqin2yrs == 1] = "y"
wekatrain[, 1] = list(NULL)
head(wekatrain)

write.csv(wekatrain, "training_balanced_weka.csv", row.names = FALSE)
