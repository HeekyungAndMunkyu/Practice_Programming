# Write file name
filename = '~/Practice_Python/DataScience/CreditScoring/test.csv'

# Load file
test = read.csv(filename, header = TRUE)
str(test)

# Check 1's and 0's
num_one = sum(test$SeriousDlqin2yrs == 1)

# Stratify
stratifiedCv = stratified(cv, "SeriousDlqin2yrs", size = num_one, replace = FALSE)
str(stratifiedCv)

# Check 1's and 0's
num_zero = sum(test$SeriousDlqin2yrs == 0)

# Save file
write.csv(stratifiedCv, "crossValidation_balanced.csv", row.names = FALSE)


