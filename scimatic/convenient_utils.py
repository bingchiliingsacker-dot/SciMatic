from typing import Literal
from decimal import Decimal, getcontext

PEMDAS = {
	'(': 1,
	')': 1,
	
	'**': 2,
	
	'*': 3,
	
	'/': 3,
	'//': 3,
	'%': 3,
	
	'+': 4,
	'-': 4
}

Operator = Literal['+', '-', '×', '•', '*', '^', '÷', '/', '//', '%', '!', '|', '(', ')', '<', '>', '<=', '>=', '==', '=', '!=', '≈', '≠']

class CreateParsable:
	def __init__(self, syntax):
		self.syntax = syntax
	
	def parse_letter(self) -> list[str]:
		output = []
		for s in self.syntax:
			if s == ' ':
				continue
			output.append(s)
		return output
	
	def parse_word(self) -> list[str]:
		output = []
		word = ''
		
		for s in self.syntax:
			if s == ' ':
				if word:
					output.append(word)
					word = ''
				continue
				
			word += s
		
		output.append(word)
		
		return output
	
	def parse_token(self) -> list:
		output = []
		word = ''
		s = self.syntax
	
		def flush():
			nonlocal word
			if word:
				try:
					output.append(int(word))
				except ValueError:
					try:
						output.append(float(word))
					except ValueError:
						output.append(word)
			word = ''
	
		i = 0
		while i < len(s):
			ch = s[i]
			if ch == ' ':
				flush()
				i += 1
				continue
			if ch in '()+-*/%':
				flush()
				if s[i:i+2] in ('**', '//'):
					output.append(s[i:i+2])
					i += 2
				else:
					output.append(ch)
					i += 1
				continue
			word += ch
			i += 1
	
		flush()
		return output

def calculate(
	expression: str,
	print_result: bool = False
) -> int | float | None:
	
	'''
	Note: calculate() was created as a safer
	alternative to eval()
	'''

	if len(expression) <= 2:
		if print_result:
			print(expression)
		return expression
	
	processor = []
	
	parsableobj = CreateParsable(expression)
	
	processor.extend(parsableobj.parse_token())
	
	def reduce_operators(processor: list[int | float | str]):
		processor = processor[:]
		while len(processor) > 1:
			try:
				highest = min(
				(token for token in processor if token in PEMDAS and token not in ('(', ')')),
				key=lambda token: PEMDAS[token]
				)
			except ValueError:
				return processor[0]
			
			index = processor.index(highest)
			left_token = processor[index - 1]
			right_token = processor[index + 1]
			operator = processor[index]
				
			if operator == '+':
				result = left_token + right_token
			elif operator == '-':
				result = left_token - right_token
			elif operator == '%':
				result = left_token % right_token
			elif operator == '//':
				result = left_token // right_token
			elif operator == '/':
				try:
					result = left_token / right_token
				except ZeroDivisionError:
					result = 0
			elif operator == '*':
				result = left_token * right_token
			elif operator == '**':
				result = left_token**right_token
			else:
				raise ValueError(f'Unsupported operator {operator}.')
				
			processor = processor[:index - 1] + [result] + processor[index + 2:]
		
		return processor[0]
	
	while '(' in processor:
		stack = []
		for i, tok in enumerate(processor):
			if tok == '(':
				stack.append(i)
				
			elif tok == ')':
				start = stack.pop()
				inner_tokens = processor[start + 1:i]
				value = reduce_operators(inner_tokens)
				processor = processor[:start] + [value] + processor[i + 1:]
				break
	
	output = reduce_operators(processor)
	
	if print_result:
		print(output)
	return output

#---------------FACTORIAL---------------#
def factorial(
	n: int,
	print_result: bool = True
) -> int | None:

	if n < 0:
		if print_result:
			print(None)
		return
	
	if n == 0:
		if print_result:
			print(1)
		return 1
	
	processor = [i for i in range(n + 1) if i != 0]
	output = []
	
	for integer in processor:
		if len(output) == 1:
			integer *= output[0]
			output = []
			
		output.append(integer)
	
	if print_result:
		print(max(output))
	return max(output)

#---------------SPECIAL VALUES---------------#
def int64_limit(
	unsigned: bool = False, 
	negative_value: bool = False
) -> int:
	
	if unsigned:
		return 2**64 - 1 if not negative_value else 0
		
	else:
		return 2**63 - 1 if not negative_value else -2**63

def pi(
	decimal: int | None = None
) -> Decimal:
	
	getcontext().prec = 100
	negative_value = False

	if decimal is None:
		output += processor
		return Decimal(output)
	
	if decimal < 0:
		decimal *= decimal
		decimal /= 2
		negative_value = True
	
	processor = '1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
	output = '3.'
	true_output = ''
	
	if decimal > 100:
		raise ValueError('Decimal parameter is higher than 100.')
	
	for i in range(int(rounded(decimal))):
		output += processor[i]

	if negative_value:
		true_output += '-'

	true_output += output
	
	return Decimal(true_output)
