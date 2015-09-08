train_sorted <- train[order(-train$DebtRatio),]
head(train_sorted,100)

train_filtered = train_sorted[15001:nrow(train_sorted),]

train_filtered = train_filtered[2:nrow(train_filtered),]
head(train_filtered$MonthlyIncome,1000)

head(train_filtered,100)

write.csv(train_filtered, "train_74352_rm_debtratio_outliers.csv", row.names = FALSE)
