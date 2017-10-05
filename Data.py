
# Read the configuration file for the Turing Machine.
# Set all the configurations for the Machine.

from TuringMachine import TuringMachine
from Instruction import Instruction

class Data:
	
	def __init__(self, filePath):
		''' Constructor. '''
		
		self.filePath = filePath # Path of the configuration file.
	
	def readAndConfigure(self, turingMachine):
		''' Read the configuration file and configure the Machine. '''
		
		confFile = None
		
		try: # Try to open the file and read all the content.
			
			confFile = open(self.filePath) # Open the conf file.
			
			# Configuration file path.
			print('Source:')
			print(self.filePath)
			
			# Comments' start.
			line = confFile.readline().strip()
			print(line + ':')
			
			# Comments.
			comments = ''
			
			# Read the comments until the end.
			while True:
				
				line = confFile.readline()
				
				if line.strip() == 'EndComments':
					
					comments = comments.strip()
					
					break
				
				comments += line
			
			print(comments)
			
			# States.
			line = confFile.readline().strip()
			print(line + ':')
			line = confFile.readline().strip()
			states = line.split(',')
			states = [elem.strip() for elem in states] # List of states' names.
			turingMachine.states = states # Set states.
			print(states)
			
			# Start state.
			line = confFile.readline().strip()
			print(line + ':')
			line = confFile.readline().strip()
			startState = line
			turingMachine.startState = startState # Set start state.
			print(startState)
			
			# Final states.
			line = confFile.readline().strip()
			print(line + ':')
			line = confFile.readline().strip()
			finalStates = line.split(',')
			finalStates = [elem.strip() for elem in finalStates]
			turingMachine.finalStates = finalStates # Set final states.
			print(finalStates)
			
			# Start table.
			line = confFile.readline().strip()
			print(line + ':')
			
			# Instructions.
			instructions = []
			
			# Read all the instructions until the end of the table.
			while True:
				
				line = confFile.readline().strip()
				
				if line == 'EndTable':
					
					break
				
				instruction = [elem.strip() for elem in line.split(',')]
				instructions.append(instruction)
				print(instruction)
				instruction = Instruction(instruction)
				turingMachine.table.add(instruction) # Add a new instruction.
			
			# Tape.
			line = confFile.readline().strip()
			print(line + ':')
			line = confFile.readline().strip()
			tape = line
			turingMachine.tape.setAll(tape) # Set the tape.
			print(tape)
		
		except:
			
			return False # Something wrong happened.
		
		return True # Nothing wrong happened.
	
# /home/patrick/Python/TuringMachine/configurations/conf.txt
