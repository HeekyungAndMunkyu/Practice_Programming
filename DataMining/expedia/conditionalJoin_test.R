test = read.csv("test.csv", header = TRUE)

nrow(test)
head(test)
colnames(test)

head(test[1])
test[,27:50] = list(NULL)
colnames(test)
write.csv(test, "test_no_comp.csv", row.names=FALSE)

test_no_comp = read.csv('test_no_comp.csv', header = TRUE)
head(test_no_comp)

summary(test)
str(test)


test$orig_destination_distance = as.numeric(test$orig_destination_distance)
test$srch_query_affinity_score = as.numeric(test$srch_query_affinity_score)
test$prop_location_score2 = as.numeric(test$prop_location_score2)
test$prop_review_score = as.numeric(test$prop_review_score)
test$visitor_hist_adr_usd = as.numeric(test$visitor_hist_adr_usd)
test$visitor_hist_starrating = as.numeric(test$visitor_hist_starrating)
test$date_time = as.numeric(test$date_time)




