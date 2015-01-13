#Guess what number between 0 and 100 I have in mind
#my code

print 'Please think of a number between 0 and 100!'
ans = ''
high = 100
low = 0
guess = 50



while ans != 'c':
	print 'Is your secret number ', guess, '?'
	print "Enter 'h' to indicate the guess is too high. ",     
	print "Enter 'l' to indicate the guess is too low. ",
	print "Enter 'c' to indicate I guessed correctly. ", 
	ans = raw_input ()

	while ans != 'c' and ans != 'h' and ans != 'l':
		print 'Sorry, I did not understand your input.'
		print 'Is your secret number ', guess, '?'
		print "Enter 'h' to indicate the guess is too high. ",
		print "Enter 'l' to indicate the guess is too low. ",
		print "Enter 'c' to indicate I guessed correctly. ",
		ans = raw_input ()

	if ans == 'c': 
		break
	elif ans == 'h':   
		high = guess
	elif ans == 'l':
		low = guess

	guess = (high + low)/2



print 'Game over. Your secret number was: ', guess







#SAMPLE CODE
print 'SAMPLE CODE'
print("Please think of a number between 0 and 100!")

# At the start the highest the number could be is 100 and the lowest is 0.
hi = 100
lo = 0
guessed = False

# Loop until we guess it correctly
while not guessed:
    # Bisection search: guess the midpoint between our current high and low guesses
    guess = (hi + lo)/2
    print("Is your secret number " + str(guess)+ "?")
    user_inp = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if user_inp == 'c':
        # We got it right!
        guessed = True
    elif user_inp == 'h':
        # Guess was too high. So make the current guess the highest possible guess.
        hi = guess
    elif user_inp == 'l':
        # Guess was too low. So make the current guess the lowest possible guess.
        lo = guess
    else:
        print("Sorry, I did not understand your input.")

print('Game over. Your secret number was: ' + str(guess))
