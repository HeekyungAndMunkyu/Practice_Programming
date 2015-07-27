stratified_1 = stratified(train_june_no_comp, "srch_id", size = 1, replace = FALSE)
write.csv(stratified_1, "train_june_no_comp_stratified.csv", row.names = FALSE)
