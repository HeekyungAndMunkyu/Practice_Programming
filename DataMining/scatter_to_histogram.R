t = wekatrain$SeriousDlqin2yrs == 'y'
str(t)

indexing = wekatrain$DebtRatio[wekatrain$SeriousDlqin2yrs == 'y']
indexing2 = indexing[indexing < 5]
hist(indexing2)
hist(indexing)
default = wekatrain$SeriousDlqin2yrs[wekatrain$SeriousDlqin2yrs == 'y']

head(indexing)
str(indexing)
head(DebtRaitoGoneDefault)
head(wekatrain)


monthincome = wekatrain$MonthlyIncome[t]
monthincome2 = monthincome[monthincome < 10000]
hist(monthincome2)
hist(monthincome)


defaultAll = wekatrain[t,]
str(defaultAll)

incomelessthan1000 = monthincome<10000
plot(defaultAll$MonthlyIncome[incomelessthan1000], defaultAll$DebtRatio[incomelessthan1000])
hist(defaultAll$age)
hist(defaultAll$RevolvingUtilizationOfUnsecuredLines)
hist(defaultAll$RevolvingUtilizationOfUnsecuredLines[defaultAll$RevolvingUtilizationOfUnsecuredLines <5])
hist(defaultAll$NumberOfOpenCreditLinesAndLoans)
hist(wekatrain$NumberOfOpenCreditLinesAndLoans)
