
# This is an elemental part of a Turing Machine.
# It contains all the instructions will use the
# Machine to work with the tape.

from Instruction import Instruction

class Table:
	
	def __init__(self):
		''' Constructor. '''
		
		self.instructions = []
	
	def search(self, stateIndex, readSymbol):
		''' Return a instruction for a state and a read symbol, if exists. '''
		
		for instruction in self.instructions:
			
			# Exists a instruction.
			if stateIndex == instruction.actualState and \
				readSymbol == instruction.readSymbol:
				
				return instruction
		
		# Not exists.
		return None
	
	def add(self, instruction):
		''' Add a new instruction. '''
		
		self.instructions.append(instruction)
	
	def __len__(self):
		''' Return the lenght of self.instructions. '''
		
		return len(self.instructions)
	
