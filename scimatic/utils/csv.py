from pathlib import Path
from typing import Any, TypeAlias
from shutil import copy
import sys

Matrix: TypeAlias = list[list[Any]]

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

class CSV:
	def __init__(self, file: str):
		self.file = Path(file)
		if self.file.suffix.lower() != '.csv':
			raise ValueError('File is not .csv.')

		self.location = PATH / self.file.name
		
		if not self.location.exists():
			self.location.touch()
	
	# Convert python matrices into csv-compatible data
	def serialize(self, matrix: Matrix, write_to_file: bool = False, print_result: bool = False) -> str:
		output = ''
		true_output = ''
		
		for m in matrix:
			for i, r in enumerate(m):
				r = str(r)
				if '"' in r:
					r = r.replace('"', '""')
				
				if ',' in r or '"' in r or '\n' in r:
					r = f'"{r}"'

				if i > 0:
					output += ','
				
				output += r
			
			output += '\n'
			true_output += output
			output = ''
		
		if write_to_file:
			self.write(true_output)
		if print_result:
			print(true_output)
		
		return true_output
	
	# Convert csv-compatible data back to python matrices
	def deserialize(self, text: str, print_result: bool = False) -> Matrix:
		processor = []
		output = []
		word = ''
		quoted = False
		skip = False
		
		for i, t in enumerate(text):
			if skip:
				skip = False
				continue
				
			if t == ',' and not quoted:
				processor.append(word)
				word = ''
				
			elif t == '\n' and not quoted:
				processor.append(word)
				output.append(processor)
				processor = []
				word = ''
				
			elif t == '"':
				if quoted:
					if i + 1 < len(text) and text[i + 1] == '"':
						word += '"'
					else:
						quoted = False
						
				else:
					quoted = True
			else:
				word += t
		
		if quoted:
			raise ValueError('Malformed CSV: unmatched quote.')
		
		if word or processor:
			processor.append(word)
			output.append(processor)
		
		if print_result:
			print(output)
		return output
	
	# writing/reading
	def read(self, print_result: bool = False) -> str:
		with self.location.open('r') as file:
			contents = file.read()
		
		if print_result:
			print(contents)
		
		return contents
	
	def write(self, new_contents: str) -> None:
		with self.location.open('w') as file:
			file.write(new_contents)
	
	def rwrite(self, new_contents: str, print_result: bool = False) -> str:
		
		with self.location.open('r+') as file:
			contents = file.read()
			file.seek(0)
			file.write(new_contents)
			file.truncate()
		
		if print_result:
			print(contents)
		
		return contents
	
	def wread(self, new_contents: str, print_result: bool = True) -> str:
		
		with self.location.open('w+') as file:
			file.write(new_contents)
			file.seek(0)
			contents = file.read()
		
		if print_result:
			print(contents)
			
		return contents
	
	# Adding/subtracting rows
	def add_row(self, new_row: Matrix | str, mode: str = 'w', print_result: bool = False) -> str | None:
		if mode not in ['w', 'r+', 'w+']:
			raise ValueError('Tip: Parameter mode follows "with" statement syntax(w, r+, w+).')
		if isinstance(new_row, list):
			new_row = self.serialize(new_row)
		
		processor = self.read()
		
		if not new_row.endswith('\n'):
			new_row = f'{new_row}\n'
		
		processor += new_row
		
		if mode == 'w':
			self.write(processor)
			return None
		elif mode == 'r+':
			output = self.rwrite(processor)
		else:
			output = self.wread(processor)
		
		if print_result:
			print(output)
		return output
	
	def delete_row(self, row_num: int = 0):
		table = self.read()
		raw = self.deserialize(table)

		if row_num < 0:
			raise ValueError('Index must be 0 or more.')
	
		if len(raw) - 1 < row_num:
			raise IndexError('Index not found...')
		
		del raw[row_num]
		
		output = self.serialize(raw)
		
		self.write(output)
	
	# Column logic
	def add_column(self, new_col: Matrix | str, mode: str = 'w', print_result: bool = False):
		if mode not in ['w', 'r+', 'w+']:
			raise ValueError('Tip: Parameter mode follows "with" statement syntax(w, r+, w+).')
		if isinstance(new_col, str):
			new_col = self.deserialize(new_col)
		
		table = self.read()
		raw = self.deserialize(table)
		height_row = len(raw)
		height_col = 0
		width = 0
		
		for r in raw:
			width = max(width, len(r))
		for n in new_col:
			height_col = max(height_col, len(n))
		
		if height_row < height_col:
			raw.extend([] for _ in range(height_col - height_row))
		
		for c in new_col:
			for j, r in enumerate(raw):
				if j >= len(c):
					break
				if width - len(r) == 0:
					r.append(c[j])
				else:
					r.extend(['' for _ in range(width - len(r))])
					r.append(c[j])

		raw = self.serialize(raw)

		if mode == 'w':
			self.write(raw)
			if print_result:
				print('Write successful!')
			return None
		elif mode == 'r+':
			output = self.rwrite(raw)
		else:
			output = self.wread(raw)
		
		if print_result:
			print(output)
		return output
		
	def delete_column(self, index: int = 0):
		raw = self.read()
		raw = self.deserialize(raw)
		if index < 0:
			raise ValueError('Index must be 0 or more.')
		for r in raw:
			if index >= len(r):
				continue
			
			del r[index]
			
		output = self.serialize(raw)
		self.write(output)
		
	# CRUD for individual cells
	def replace_cell(self, coordinates: tuple[int, int], value: Any):
		
		
		raw = self.read()
		processor = self.deserialize(raw)
		if coordinates[0] < 0 or coordinates[1] < 0:
			raise ValueError('Coordinates must be 0 or more.')
		if coordinates[1] >= len(processor):
			raise ValueError('Coordinates out of range.')
		
		if coordinates[0] >= len(processor[coordinates[1]]):
			raise ValueError('Coordinates out of range.')
		
		for i, p in enumerate(processor):
			if i == coordinates[1]:
				p[coordinates[0]] = str(value)
		
		processor = self.serialize(processor)
		self.write(processor)
	
	def delete_cell(self, coordinates: tuple[int, int]):
		raw = self.read()
		processor = self.deserialize(raw)
		
		if coordinates[0] < 0 or coordinates[1] < 0:
			raise ValueError('Coordinates must be 0 or more.')
			
		if coordinates[1] >= len(processor):
			raise ValueError('Coordinates out of range.')
		
		if coordinates[0] >= len(processor[coordinates[1]]):
			raise ValueError('Coordinates out of range.')
		
		for i, p in enumerate(processor):
			if i == coordinates[1]:
				del p[coordinates[0]]
		
		processor = self.serialize(processor)
		self.write(processor)

	# Safely modify file by duplicating it
	# SciMatic convention uses brackets instead of parentheses: example[1].csv instead of example(1).csv
	
	def dup(self, name: str | None = None, ndups: int = 1):
		if ndups < 1:
			raise ValueError('ndups must be at least 1.')
	
		if name is not None:
			if not name.endswith('.csv'):
				name = f'{name}.csv'
			
			destination = PATH / name
			copy(self.location, destination)
		
			return None
		
		template = self.file.stem
		
		# If the filename already has [N], extract N
		if '[' in template and ']' in template:
			processor = ''
			enum = False
			for t in template:
				if t == '[':
					enum = True
					continue
				if t == ']':
					enum = False
					continue
				if enum and t.isdigit():
					processor += t
			if processor:
				n = int(processor) + 1
				template = template[:template.rfind('[')]
			else:
				n = 1
		else:
			n = 1
		
		for _ in range(ndups):
			filename = f'{template}[{n}].csv'
			destination = PATH / filename
			
			# Don't overwrite an existing duplicate
			while destination.exists():
				n += 1
				filename = f'{template}[{n}].csv'
				destination = PATH / filename
		
			copy(self.location, destination)
			n += 1