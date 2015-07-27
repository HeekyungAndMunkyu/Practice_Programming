originalData = read.csv("train_june_no_comp_stratified.csv", header = TRUE)

originalData$click_bool[originalData$click_bool == 1] = "yes"
originalData$click_bool[originalData$click_bool == 0] = "no"

str(originalData)

write.csv(originalData, "train_target_click_bool.csv", row.names = FALSE)
