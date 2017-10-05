
# It contains a little rule about what to do in 
# case the Machine read a specific symbol.
# It's related to a State.

class Instruction:
	
	def __init__(self, data):
		''' Constructor. '''
		
		self.actualState = data[0] # Actual state.
		self.readSymbol = data[1] # Read symbol.
		self.nextState = data[2] # Next state.
		self.direction = data[3] # Head direction.
		self.newSymbol = data[4] # New symbol to write.
	
