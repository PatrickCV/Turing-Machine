
# This is an elemental part of a Turing Machine.
# It can read and write symbols on the tape.

from Tape import Tape

class Head:
	
	def __init__(self):
		''' Constructor. '''
		
		self.position = 10
		self.stopped = False
	
	def write(self, tape, symbol):
		''' Write a symbol in the tape. '''
		
		tape.set(symbol, self.position)
		
	def read(self, tape):
		''' Read the symbol that is in the head position. '''
		
		return tape.get(self.position)
	
	def move(self, tape, direction):
		''' Move the head. '''
		
		if direction == '<': # Left.
				
			self.goLeft(tape)
		
		elif direction == '>': # Right.
			
			self.goRight(tape)
		
		elif direction == '-': # Stop.
			
			self.stop()
	
	def goLeft(self, tape):
		''' Move the head to left. '''
		
		# In the position 10.
		if self.position == 10:
			
			# Create a new blank symbol at the tail of the tape.
			tape.addHead('B')
		
		else:
			
			self.position -= 1
	
	def goRight(self, tape):
		''' Move the head to right. '''
		
		# In the -10 position.
		if self.position == (tape.get(len(tape) -10)):
			
			# Create a new blank symbol at the head of the tape.
			tape.addTail('B')
		
		self.position += 1
		
	def stop(self):
		''' Stop the head. '''
		
		self.stopped = True
	
	def isStopped(self):
		''' Verify if the head is stopped. '''
		
		return self.stopped
