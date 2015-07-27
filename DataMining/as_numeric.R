# Wrtie file name
filename = '~/Workspace/train.csv'
# read file
train = read.csv(filename, header = TRUE)
str(train)
# convert target to nominal
train$booking_bool[train$booking_bool == 1] = "yes"
train$booking_bool[train$booking_bool == 0] = "no"
# convert input values to numeric
train$gross_bookings_usd = as.numeric(train$gross_bookings_usd)
train$orig_destination_distance = as.numeric(train$orig_destination_distance)
train$srch_query_affinity_score = as.numeric(train$srch_query_affinity_score)
train$prop_location_score2 = as.numeric(train$prop_location_score2)
train$prop_review_score = as.numeric(train$prop_review_score)
train$visitor_hist_adr_usd = as.numeric(train$visitor_hist_adr_usd)
train$visitor_hist_starrating = as.numeric(train$visitor_hist_starrating)
train$date_time = as.numeric(train$date_time)
train$click_bool = as.numeric(train$click_bool)
# save file
write.csv(train, "train_click_numeric.csv", row.names = FALSE)


colnames(train)
train[,29:30] = list(NULL)
