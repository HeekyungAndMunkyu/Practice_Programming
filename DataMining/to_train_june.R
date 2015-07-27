as.character(data$date_time[c(1, nrow(data))]) # as.character를 하지 않으면 factor연산이 엄청남.
date_data = data.frame(date = as.numeric(substr(gsub("-", "", data$date_time), 1, 8)))
head(date_data)
rownames(date_data) = NULL
date_data_2 = data.frame(date = sort(unique(date_data$date), decreasing = FALSE))
head(date_data_2, 3)
tail(date_data_2, 3)
nrow(date_data_2)
fix(date_data_2)
date_data = data.frame(date = as.numeric(substr(gsub("-", "", data$date_time), 1, 8)))
date_data_table = data.frame(table(sort(date_data$date, decreasing = FALSE)))
data_frame = data.frame(data)
data_frame_sorted = data_frame[order(data$date_time),]
head(data_frame_sorted)
tail(data_frame_sorted)
data_sliced = data_frame_sorted[8439848:9917530,]
head(data_sliced,20)
write.csv(data_sliced, "train_june.csv", row.names=FALSE)
