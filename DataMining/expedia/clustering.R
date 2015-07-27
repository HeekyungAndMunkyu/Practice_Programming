clustered = read.csv("clusteredCSV_no_instance_num.csv", header = TRUE)
head(clustered)


cluster2 = clustered[clustered$Cluster == 'cluster2',]
head(cluster2)
write.csv(cluster2, "cluster2.csv", row.names = FALSE)

originalData = read.csv("train_june_no_comp_stratified.csv", header = TRUE)
head(originalData)
id_booking = originalData[c('srch_id', 'booking_bool')]
head(id_booking)

cluster0_merged = merge(cluster0, id_booking, by = 'srch_id')
head(cluster0_merged)
write.csv(cluster0_merged, "cluster0.csv", row.names = FALSE)

cluster1_merged = merge(cluster1, id_booking, by = 'srch_id')
head(cluster1_merged)
write.csv(cluster1_merged, "cluster1.csv", row.names = FALSE)

cluster2_merged = merge(cluster2, id_booking, by = 'srch_id')
head(cluster2_merged)
write.csv(cluster2_merged, "cluster2.csv", row.names = FALSE)

cluster2_check = read.csv("cluster2.csv", header = TRUE)
head(cluster2_check)
