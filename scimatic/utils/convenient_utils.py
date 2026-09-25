from typing import Literal
from decimal import Decimal, getcontext
from pathlib import Path
import json
import sys

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

def _default_path() -> Path:
	if sys.platform == 'win32':
		return Path.home() / 'Downloads'

	if sys.platform == 'android' or Path('/storage/emulated/0').exists():
		return Path('/storage/emulated/0') / 'Download'

	# Linux/macOS: honor XDG if set, else fall back to ~/Downloads
	import os
	xdg = os.environ.get('XDG_DOWNLOAD_DIR')
	return Path(xdg) if xdg else Path.home() / 'Downloads'


PATH = _default_path()
PATH.mkdir(parents=True, exist_ok=True)

class CreateParsable:
	def __init__(self, syntax):
		self.syntax = syntax

	def parse_letter(self, print_result=False) -> list[str]:
		output = []

		for s in self.syntax:
			if s == ' ':
				continue

			output.append(s)

		if print_result:
			print(output)

		return output

	def parse_word(self, print_result=False) -> list[str]:
		output = []
		word = ''

		for s in self.syntax:
			if s == ' ':
				if word:
					output.append(word)
					word = ''
				continue

			word += s

		if word:
			output.append(word)

		if print_result:
			print(output)

		return output

	def parse_token(self, print_result=False) -> list:
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

			if ch == '-' and i + 1 < len(s):
				next_char = s[i + 1]

				if (
					next_char.isdigit()
					or next_char == '-'
				) and (
					not output
					or (
						isinstance(output[-1], str)
						and output[-1] in '()+-*/%'
					)
				):
					word += ch
					i += 1
					continue

			if ch in '()+-*/%':
				flush()

				if s[i:i + 2] in ('**', '//'):
					output.append(s[i:i + 2])
					i += 2
				else:
					output.append(ch)
					i += 1

				continue

			word += ch
			i += 1

		flush()

		if print_result:
			print(output)

		return output

	def parse_kwargs(
		self,
		save_json: bool = False,
		print_result: bool = False
	) -> dict:

		if self.syntax.find('=') == -1:
			raise ValueError(
				f'Text invalid: \'=\' expected, got \'{self.syntax}\'.'
			)

		value = ''
		val_num = 0
		key = ''
		output = {}
		equal = False
		quoted = False

		for s in self.syntax:
			if s == '"' and not quoted:
				quoted = True
				continue

			elif s == '"' and quoted:
				quoted = False
				continue

			if s == '=':
				if not key:
					raise KeyError('Expected key argument, got None.')
				else:
					equal = True
					continue

			if s == '"':
				quoted = True

			if s == ' ' and not quoted:
				if not value:
					output[key] = None
				else:
					try:
						val_num = int(value)
					except ValueError:
						try:
							val_num = float(value)
						except ValueError:
							output[key] = value
							key = ''
							value = ''
							equal = False
							continue

					output[key] = val_num

				key = ''
				value = ''
				val_num = 0
				equal = False
				continue

			if not equal:
				key += s
			else:
				value += s

		if key:
			if not value:
				output[key] = None
			else:
				try:
					val_num = int(value)
					output[key] = val_num
				except ValueError:
					try:
						val_num = float(value)
						output[key] = val_num
					except ValueError:
						output[key] = value

		if 'json' not in output and save_json:
			raise ValueError('No json key argument given.')

		if 'json' in output and save_json:
			if output['json'] is None:
				print('Tip: File cannot be None.')
				print('No JSON file found.')
				raise FileNotFoundError(
					'Key argument json does not have a file.'
				)

			location = PATH / output['json']

			if not location.exists():
				location.touch()

			with location.open('w') as f:
				del output['json']
				json.dump(output, f)

		if print_result:
			print(output)

		return output


def exponentiate_right(*args):
	output = args[-1]

	for a in args[-2::-1]:
		output = a**output

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
		try:
			int(expression)
		except ValueError:
			try:
				float(expression)
			except ValueError:
				return expression
		return expression

	processor = []

	parsableobj = CreateParsable(expression)

	processor.extend(parsableobj.parse_token())

	def reduce_operators(processor: list[int | float | str]):
		processor = processor[:]

		while len(processor) > 1:
			try:
				highest = min(
					(
						token
						for token in processor
						if token in PEMDAS
						and token not in ('(', ')')
					),
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
					raise ZeroDivisionError('Tip: Do not divide by 0')

			elif operator == '*':
				result = left_token * right_token

			elif operator == '**':
				tower = [left_token, right_token]
				current = index

				while current + 2 < len(processor):
					if processor[current + 2] == operator:
						current += 2
						tower.append(processor[current + 1])
					else:
						break

				if len(tower) == 2:
					result = left_token**right_token
				else:
					result = exponentiate_right(*tower)

				processor = (
					processor[:index - 1]
					+ [result]
					+ processor[current + 2:]
				)
				continue

			else:
				raise ValueError(
					f'Unsupported operator {operator}.'
				)

			processor = (
				processor[:index - 1]
				+ [result]
				+ processor[index + 2:]
			)

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

				processor = (
					processor[:start]
					+ [value]
					+ processor[i + 1:]
				)
				break

	output = reduce_operators(processor)

	if print_result:
		print(output)

	return output
#---------------FACTORIAL---------------#
def factorial(
	n: int,
	print_result: bool = False
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
        negative_value: bool = False,
        print_result: bool = False
) -> int:

        if unsigned:
                output = 2**64 - 1 if not negative_value else 0

        else:
                output = 2**63 - 1 if not negative_value else -2**63
        
        if print_result:
        	print(output)
        return output

def int32_limit(
        unsigned: bool = False, 
        negative_value: bool = False,
        print_result: bool = False
) -> int:

        if unsigned:
                output = 2**32 - 1 if not negative_value else 0

        else:
                output = 2**31 - 1 if not negative_value else -2**31
        
        if print_result:
        	print(output)
        return output

def int16_limit(
        unsigned: bool = False, 
        negative_value: bool = False,
        print_result: bool = False
) -> int:

        if unsigned:
                output = 2**16 - 1 if not negative_value else 0

        else:
                output = 2**15 - 1 if not negative_value else -2**15
        
        if print_result:
        	print(output)
        return output

def int8_limit(
        unsigned: bool = False, 
        negative_value: bool = False,
        print_result: bool = False
) -> int:

        if unsigned:
                output = 2**8 - 1 if not negative_value else 0

        else:
                output = 2**7 - 1 if not negative_value else -2**7
        
        if print_result:
        	print(output)
        return output

def pi(
        decimal: int | None = None,
        print_result: bool = False
) -> Decimal:

    getcontext().prec = 100
    negative_value = False

    processor = '1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
    output = '3.'
    true_output = ''

    if decimal is None:
        output += processor

        if print_result:
            print(output)

        return Decimal(output)

    if decimal < 0:
        decimal = abs(decimal)
        negative_value = True

    if decimal > 100:
        raise ValueError('Decimal parameter is higher than 100.')

    for i in range(int(round(decimal))):
        output += processor[i]

    if negative_value:
        true_output += '-'

    true_output += output

    if print_result:
        print(true_output)

    return Decimal(true_output)