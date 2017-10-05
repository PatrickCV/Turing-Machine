
from TuringMachine import TuringMachine
from Interface import Interface

if __name__ == '__main__':
	
	turingMachine = TuringMachine()
	interface = Interface(turingMachine)
	
	interface.start()
	
