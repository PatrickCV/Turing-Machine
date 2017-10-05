
# A simple console interface.
# Get the configuration file path and start the Turing Machine.

import os

from State import State
from Instruction import Instruction
from Table import Table
from TuringMachine import TuringMachine
from Data import Data

class Interface:
	
	def __init__(self, turingMachine):
		''' Constructor. '''
		
		self.turingMachine = turingMachine
		self.clearCommand = 'cls' if os.name == 'nt' else 'clear'
	
	def clear(self):
		''' Clear the console. '''
		
		os.system(self.clearCommand)
		os.system(self.clearCommand)
	
	def start(self):
		''' Start the interface. '''
		
		self.clear()
		self.menu()
	
	def menu(self):
		''' Show the application's menu. '''
		
		print('The Turing Machine')
		print()
		print('1. Start a Turing Machine')
		print('2. Exit')
		
		option = input()
		
		if option == '1': # Start a Turing Machine.
			
			self.clear()
			self.configureMachine()
		
		elif option == '2': # Exit.
			
			print('Bye')
		
		else: # Something else.
			
			self.clear()
			self.menu()
	
	def showNearestSymbols(self):
		''' Show the nearest head symbols. '''
		
		headPosition = self.turingMachine.head.position
		tape = self.turingMachine.tape.getAll()
		tapeSlice = tape[(headPosition -10) : (headPosition + 11)]
		
		tapeSlice = ''.join(tapeSlice)
		
		print(tapeSlice)
	
	def configureMachine(self):
		''' Set the configurations of the Turing Machine. '''
		
		print('Note:')
		print('Follow this structure in the file:\n')
		print('Comments')
		print('-Write some comments.-')
		print('EndComments')
		print('States')
		print('-Write the states\' names, separated by coma.-')
		print('Start State')
		print('-Write the start state name.-')
		print('Final States')
		print('-Write the final states\' names, separated by coma.-')
		print('Table')
		print('-Specify the instructions, one for line.-')
		print('-Order of the instruction\'s parts:-')
		print('-actualState, readSymbol, nextState, direction, newSymbol-')
		print('EndTable')
		print('Tape')
		print('-Write here the tape-\n')
		print('See an example in /configurations/conf.txt\n')
		
		while True:
			
			# Catch the file.
			filePath = input('File path: ').strip()
			data = Data(filePath)
			
			itsOk = data.readAndConfigure(self.turingMachine)
			
			if itsOk: # Nothing wrong happened.
				
				break
			
			else: # Something wrong happened.
				
				print('Something wrong happened with the file.')
		
		input('\n<Enter> to continue.')
		
		self.clear()
		
		self.lifeCycle()
	
	def lifeCycle(self):
		''' Do all the steps of the Machine. '''
		
		# Prepare the Machine.
		self.turingMachine.beforeStart()
		
		while True:
			
			# Capture the actual state.
			stateRegister = self.turingMachine.stateRegister
			actualState = stateRegister.name
			
			print('Actual State:', actualState)
			print()
			
			# Show the head.
			print((' ' * 9), 'V')
			
			# Show the nearest head symbols.
			self.showNearestSymbols()
			
			if self.turingMachine.isCrashed:
				
				print('Crashed!')
				
				break
			
			if self.turingMachine.isFinished:
				
				print('Finished!')
				
				break
			
			print()
			input('<Enter> to the next step.')
			
			# Do the next step.
			self.turingMachine.step()
			
			self.clear()
		
		
		
		
		
		## Cycle of steps
		#while True:
			
			#if self.turingMachine.isCrashed:
				
				#print('Crashed!')
				
				#break
			
			#if self.turingMachine.isFinished:
				
				#print('Finished!')
				
				#break
			
			## Capture the actual state.
			#stateRegister = self.turingMachine.stateRegister
			#actualState = stateRegister.name
			
			#print('Actual State:', actualState)
			#print()
			
			## Show the head.
			#print((' ' * 9), 'V')
			
			## Show the nearest head symbols.
			#self.showNearestSymbols()
			
			#print()
			#input('<Enter> to the next step.')
			
			## Do the next step.
			#self.turingMachine.step()
			
			#self.clear()
