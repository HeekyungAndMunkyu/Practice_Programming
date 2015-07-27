filename = '~/Workspace/Expedia/test989_clustered.csv'

clustered = read.csv(filename, header = TRUE)
head(clustered)

str(unique(clustered['srch_id']))
str(unique(cluster0['srch_id']))

cluster1[c('Instance_number', 'Cluster')] = list(NULL)
str(cluster0)

cluster0 = clustered[clustered$Cluster == 'cluster0',]
str(cluster0)
cluster0['click_bool'] ='yes'
cluster0[c('Cluster')] = list(NULL)
write.csv(cluster0, "test_cluster0.csv", row.names = FALSE)

onlyClick = clustered[c('srch_id', 'prop_id', 'click_bool')]
head(onlyClick)

cluster0_merged = merge(cluster0, onlyClick, by = c('srch_id', 'prop_id'))
head(cluster0_merged)
write.csv(cluster0_merged, "cluster0.csv", row.names = FALSE)

cluster1_merged = merge(cluster1, onlyClick, by = 'srch_id')
head(cluster1_merged)
write.csv(cluster1_merged, "cluster1.csv", row.names = FALSE)

cluster2_merged = merge(cluster2, onlyClick, by = 'srch_id')
head(cluster2_merged)
write.csv(cluster2_merged, "cluster2.csv", row.names = FALSE)
