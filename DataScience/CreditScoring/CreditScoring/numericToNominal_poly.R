trainPoly = read.csv("~/Practice_Python/DataScience/CreditScoring/test_poly.csv", header = FALSE)

trainPoly$V67[trainPoly$V67 == 0] = "n"
trainPoly$V67[trainPoly$V67 == 1] = "y"

head(trainPoly)

write.csv(trainPoly, "poly_training_weka.csv", row.names = FALSE)
