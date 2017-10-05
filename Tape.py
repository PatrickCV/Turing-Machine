
# This is an elemental part of a Turing Machine.
# It contains a sequence of symbols that the Machine
# will use to read and write.

class Tape:
	
	def __init__(self):
		''' Constructor. '''
		
		# All the symbols of the tape.
		self.symbols = []
	
	def setAll(self, all):
		''' Set all the tape. '''
		
		# Head and tail of blank symbols.
		self.symbols = list('B' * 10) + list(all) + list('B' * 10)
	
	def set(self, symbol, position):
		''' Change a symbol on a position for other. '''
		
		self.symbols[position] = symbol
	
	def getAll(self):
		''' Return all the tape. '''
		
		return self.symbols
	
	def get(self, position):
		''' Return a symbol on a position. '''
		
		return self.symbols[position]
	
	def addTail(self, symbol):
		''' Add a new symbol at the tail. '''
		
		self.symbols.append(symbol)
	
	def addHead(self, symbol):
		''' Add a new symbol at the head. '''
		
		self.symbols = [symbol] + self.symbols
	
	def __len__(self):
		''' Return the lenght of self.symbols. '''
		
		return len(self.symbols)
