#l4
#towers of hanoi
#three towers
#move discs to another tower


def moves(disc):
	'''
	disc: int >= 1 (number of discs)

	returns: int, the number of moves to move all discs to another tower
	'''

	if disc == 1:
		return 1
	return 1 + 2 * moves(disc - 1)

def printMove(fr, to):
	'''
	fr, to: str (from where to where)

	returns: direction of a move
	'''
	
	print 'Move from ' + str(fr) + ' to ' + str(to) + '.'

def direction(disc, fr, to, sp):
	'''
	disc: int >= 1 (number of discs)
	fr, to, sp: str

	returns: every direction of moves
	'''

	if disc == 1:
		printMove(fr, to)

	else:
		direction(disc - 1, fr, sp, to)
		direction(1, fr, to, sp)
		direction(disc - 1, sp, to, fr)



disc = int(raw_input('How many discs are around the towers of Hanoi?'))

print 'For', disc, 'discs,', moves(disc), 'moves are required.'
print ''
print direction(disc, 'F', 'T', 's')
print ''
print 'The end.'
