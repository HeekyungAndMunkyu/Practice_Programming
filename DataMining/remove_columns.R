# check file
nrow(train_june)
head(train_june)
colnames(train)
head(train[1])

# remove unnecessary attributes (comp_rate1 ~ 8)
train[,28:51] = list(NULL)
colnames(train_june)

# save file
write.csv(train_june, "train_june_no_comp.csv", row.names=FALSE)











train_june_no_comp = read.csv('train_june_no_comp.csv', header = TRUE)
head(train_june_no_comp)

test1000 = test[1:989, ]
write.csv(test1000, "test989.csv", row.names=FALSE)
summary(test1000)
str(test1000)

tail(test1000, 20)

train_c0_100 = train_cluster0[1:100, ]
write.csv(train_c0_100, "cluster0_100.csv", row.names = FALSE)
str(train_c0_100)
train_c0_100[c('Cluster', 'position')]= list(NULL)
