#2-1. Paying the Minimum
#Write a program to calculate the credit card balance after 12 months
#if a person only pays the minimum monthly payment.
#balance/ annualInterestRate/ monthlyPaymentRate will be handled by the instructor

balance = float(raw_input('balance: '))
annualInterestRate = float(raw_input('annual Interest Rate: '))
monthlyPaymentRate = float(raw_input('monthly Payment Rate: '))


month = 0.00
monthlyPayment = 0.00
monthlyInterestRate = annualInterestRate/12.0
totalPaid = 0.00

for i in range(1,13):
	month = i
	monthlyPayment = balance * monthlyPaymentRate
	balance = balance - monthlyPayment
	
	totalPaid += monthlyPayment

	balance = balance * ( 1 + monthlyInterestRate)


	print 'Month:', month
	print 'Minimum monthly payment:', round(monthlyPayment, 2)
	print 'Remaining balance:', round(balance, 2)



print 'Total paid:', round(totalPaid, 2) 
print 'Remaining balance:', round(balance, 2)
