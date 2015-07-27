filename = '~/Workspace/Expedia/train_stratified_balanced.csv'

stratifiedData = read.csv(filename, header = TRUE)

click_yes = sum(train$click_bool == "yes")
sum(train$booking_bool == "no")
str(stratifiedData)

stratified2 = stratified(stratifiedData, "click_bool", size = 30000, replace = FALSE)

str(stratified2)

write.csv(stratified2, "train_stratified_balanced.csv", row.names = FALSE)

sum(stratified$click_bool == "no")
colnames(stratified)
stratified2[,29:30] = list(NULL)

write.csv(stratified2, "train_stratified_balanced_click.csv", row.names = FALSE)

