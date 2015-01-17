#2-2. Paying Debt off in a Year
#Write a program calculating the minimum fixed monthly payment needed
#in order to pay off a credit card balance in 12 months.
#balance & annualInterestRate will be handled by the instructor.

balance = float(raw_input('balance = '))
annualInterestRate = float(raw_input('annual interest rate = '))





monthlyInterestRate = annualInterestRate/12.0
print 'monthlyInterestRate: ',monthlyInterestRate
monthlyPayment = 0

while True:
	monthlyPayment += 10
	remainingBalance = balance
	for i in range(1, 13):
		remainingBalance = remainingBalance - monthlyPayment
		remainingBalance = remainingBalance * (1 + monthlyInterestRate)
		print 'remaining balance: ', remainingBalance
	print 'monthlyPayment =', monthlyPayment, 'balance =', remainingBalance
	if remainingBalance <= 0: 
		break

print 'Lowest Payment:', monthlyPayment
