
# It's the Machine.

from StateRegister import StateRegister
from Tape import Tape
from Head import Head
from Table import Table

class TuringMachine:
	
	def __init__(self):
		''' Constructor. '''
		
		self.stateRegister = StateRegister() # The state register.
		self.tape = Tape() # The tape.
		self.head = Head() # The head.
		self.table = Table() # The table.
		self.states = [] # The states.
		self.startState = '' # Start state.
		self.finalStates = [] # Final states.
		
		self.isFinished = False # It's over?.
		self.isCrashed = False # Ops or not ops.
		
	def beforeStart(self):
		''' Prepare the Machine before it start. '''
		
		# Set the state register to the start state.
		self.stateRegister.name = self.startState
		
	def step(self):
		''' Do a little step of the Turing Machine.
		It's the most important part. '''
		
		# State register is in the final states.
		if self.stateRegister.name in self.finalStates:
			
			self.isFinished = True
			
			return
		
		# Read the symbol.
		readSymbol = self.head.read(self.tape)
		
		# Actual state.
		actualState = self.stateRegister.name
		
		# Search the corresponding instruction, if exists.
		instruction = self.table.search(actualState, readSymbol)
		
		# There's not an instruction for the read symbol (crash).
		if instruction == None:
			
			#print('Paso')
			self.isCrashed = True
			
			return
		
		# Write the new symbol.
		newSymbol = instruction.newSymbol
		self.head.write(self.tape, newSymbol)
		
		# Change the head position.
		if not self.head.isStopped(): # Not stopped.
			
			# Move the head.
			self.head.move(self.tape, instruction.direction)
			
		else: # Is stopped.
			
			self.isFinished = True
			
			return
		
		# Change the actual state (state register).
		self.stateRegister.name = instruction.nextState
