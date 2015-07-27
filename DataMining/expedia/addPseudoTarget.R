# write file name
filename = '~/Workspace/Expedia/test989_clustered.csv'

# load file
clustered = read.csv(filename, header = TRUE)
head(clustered)

# remove meaningless attributes
cluster1[c('Instance_number', 'Cluster')] = list(NULL)
str(cluster0)

# split data into clusters
cluster0 = clustered[clustered$Cluster == 'cluster0',]
str(cluster0)

# add pseudo target
cluster0['click_bool'] ='yes'

# save file
write.csv(cluster0, "test_cluster0.csv", row.names = FALSE)
