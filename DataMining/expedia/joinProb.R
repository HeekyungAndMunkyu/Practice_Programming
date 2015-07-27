prob = read.csv("prob_cluster0.csv", header = FALSE)
head(prob)
str(prob)

cluster0_prob = cbind(cluster0, prob)
str(cluster0_prob)

write.csv(cluster0_prob, "probability_cluster0.csv", row.names = FALSE)
