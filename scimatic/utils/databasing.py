from typing import Callable, Any
import sqlite3
from pathlib import Path
from platformdirs import user_data_dir
from datetime import datetime
from .. import __version__

#---------Redirect .db file to virtual environment
DATA_DIR = Path(user_data_dir('SciMatic'))
DATA_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DATA_DIR / 'data.db'

class Database:
	
	def __init__(self):
		self.date = datetime.now().strftime('%m/%d/%Y')
		self.conn = sqlite3.connect(DB_PATH)
		self.cursor = self.conn.cursor()
		
		self.cursor.execute('''
		CREATE TABLE IF NOT EXISTS data (
			id INTEGER PRIMARY KEY,
			date TEXT,
			function_ran TEXT,
			value TEXT,
			version TEXT
			)
		''')

		self.conn.commit()
		
	# Decorator function
	def store(self, func: Callable) -> Callable:
		def wrapper(*args, **kwargs) -> Any:
			result = func(*args, **kwargs)
			
			self.cursor.execute('INSERT INTO data (date, function_ran, value, version) VALUES (?, ?, ?, ?)',
			(self.date, func.__name__, str(result), __version__)
			)
			
			self.conn.commit()
			
			return result
		
		return wrapper
	
	def get_one(self, id: int | None = None, print_result: bool = False) -> tuple[int, str, str, str, str] | None:
		if id is None:
			self.cursor.execute('''
			SELECT * FROM data
			ORDER BY id DESC
			LIMIT 1
			''')
		else:
			self.cursor.execute(
			'SELECT * FROM data WHERE id = ?',
			(id, )
			)
		
		result = self.cursor.fetchone()
		
		if result is None:
			if print_result:
				if id is None:
					print('Database is empty. Maybe you can initialize it before running.')
				else:
					print(f'Id number {id} does not exist.')
			return None
		
		if print_result:
			print(f'ID: {result[0]}\tDate stored: {result[1]}\tFunction: {result[2]}\tReturn Value: {result[3]}\tVersion: {result[4]}')
		return result
	
	def get_all(self, print_result: bool = False) -> list[tuple[int, str, str, str, str]]:
		
		self.cursor.execute('SELECT * FROM data')
		
		records = self.cursor.fetchall()
		
		if not records:
			if print_result:
				print('Database is empty. Maybe you can initialize it before running.')
			return []
		
		if print_result:
			for r in records:
				print(f'ID: {r[0]}\tDate stored: {r[1]}\tFunction: {r[2]}\tReturn Value: {r[3]}\tVersion: {r[4]}')
		return records
	
	def delete(self, id: int | None = None, print_result: bool = False) -> None:
		if id is None:
			self.cursor.execute('''
				SELECT * FROM data
				ORDER BY id DESC
				LIMIT 1
			''')
		else:
			self.cursor.execute('SELECT * FROM data WHERE id = ?',
			(id, )
			)
		
		result = self.cursor.fetchone()
		
		if result is None:
			if print_result:
				if id is None:
					print('Database is empty. Maybe you can initialize it before running.')
				else:
					print(f'Id number {id} does not exist.')
			return None
		
		self.cursor.execute('DELETE FROM data WHERE id = ?',
		(result[0], )
		)
		
		self.conn.commit()
		
		if print_result:
			print(f'Deleted ID: {result[0]}')
		return None
	
	def reset(self, print_result: bool = False) -> None:
		self.cursor.execute('DELETE FROM data')
		self.conn.commit()
		
		if print_result:
			print('Database reset successfully.')
		return None
