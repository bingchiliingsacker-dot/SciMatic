from typing import Literal
from .errors import ModeError


Operator = Literal['+', '-', '×', '•', '*', '^', '÷', '/', '//', '%', '!', '|', '(', ')', '<', '>', '<=', '>=', '==', '=', '!=', '≈', '≠']

def parser(
	raw_syntax: str,
	mode: str = 'letter',
	print_result: bool = True
) -> list[int] | list[str] | None:
	
	modes = ['letter', 'word', 'token']
	processor = []
	output = []
	token_output = []
	word = ''
	
	if mode not in modes:
		raise ModeError(f'Mode is not in modes: {modes}')
	
	for letter in raw_syntax:
		processor.append(letter)
	
	if mode == modes[0]:
		for p in processor:
			if p == ' ':
				continue
			output.append(p)
		
	else:
		for p in processor:
			if p == ' ':
				if word:
					output.append(word)
					word = ''
				continue
				
			word += p
		
		if word:
			output.append(word)
		
		if mode == modes[2]:
			for o in output:
				try:
					syn = int(o)
				except ValueError:
					try:
						syn = float(o)
					except ValueError:
						syn = o
						
				token_output.append(syn)
			
			output = token_output
	
	if print_result:
		print(output)
	return output
