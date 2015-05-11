#2-3.Paying Debts off in a Year - use Bisection Search
#write a program that calculates fixed monthly payment which pays off debts in a year
#balance(debt) & annualInterestRate will be given

balance = float(raw_input('balance = '))
annualInterestRate = float(raw_input('annual interest rate = '))

monthlyInterestRate = annualInterestRate/12.0
low = balance/12.0
high = (balance * (1 + monthlyInterestRate)**12)/12.0
monthlyPayment = (high + low)/2.0


while True:
	remainingBalance = balance
	monthlyPayment = (high + low)/2.0

	for i in range(1, 13):
		remainingBalance -= monthlyPayment
		remainingBalance *= (1 + monthlyInterestRate)
	if remainingBalance > 0:
		low = monthlyPayment
	elif remainingBalance < 0:
		high = monthlyPayment
	else:
		break


	if remainingBalance <=0 and remainingBalance > -0.01:
		break

print 'Lowest Payment:', round(monthlyPayment, 2)
