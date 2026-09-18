import requests
from functools import cache
import sqlite3
from pathlib import Path
from platformdirs import user_data_dir

DATA_DIR = Path(user_data_dir('SciMatic'))
DATA_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DATA_DIR / 'saved_currencies.db'

def fresh_convert_curr(
	money: float,
	curr1: str,
	curr2: str,
	id: int | None = None,
	save_offline: bool = True,
	use_offline_db: bool = False,
	reset_db: bool = False,
	print_result: bool = False
	) -> float | None:
	
	curr1 = curr1.upper()
	curr2 = curr2.upper()
	
	conn = sqlite3.connect(DB_PATH)
	cursor = conn.cursor()
	
	if reset_db:
		try:
			cursor.execute('DELETE FROM saved_currencies')
			conn.commit()
		except sqlite3.OperationalError:
			if print_result:
				print('Database reset failed: Database does not exist yet.')
			return None
		finally:
			conn.close()
		
		if print_result:
			print('Database reset.')
		return None
	
	if use_offline_db:
		try:
			if id is None:
				cursor.execute('SELECT * FROM saved_currencies WHERE currency1 = ? AND currency2 = ?',
				(curr1, curr2)
				)
				
			else:
				cursor.execute('SELECT * FROM saved_currencies WHERE id = ? AND currency1 = ? AND currency2 = ?',
				(id, curr1, curr2)
				)
				
		except sqlite3.OperationalError:
			if print_result:
				print('Database is empty and may need some initiation.')
			conn.close()
			return None

		row = cursor.fetchone()
		
		if row is not None:
			data = row[3]
			output = data * money
			
			if print_result:
				print(f'{money}{curr1} -> {output}{curr2}')
			return output
		else:
			conn.close()
			return None
	
	try:
		url = f'https://api.frankfurter.dev/v2/rate/{curr1}/{curr2}'
		response = requests.get(url)
		response.raise_for_status()
		
		data = response.json()['rate']
	except requests.RequestException:
		if print_result:
			print('Something went wrong... Perhaps you misspelled something.')
		return None
	
	if save_offline:
		cursor.execute('''
		CREATE TABLE IF NOT EXISTS saved_currencies (
			id INTEGER PRIMARY KEY,
			currency1 TEXT,
			currency2 TEXT,
			rate REAL
		)
		''')
		
		cursor.execute('INSERT INTO saved_currencies (currency1, currency2, rate) VALUES (?, ?, ?)',
		(curr1, curr2, data)
		)
		
		conn.commit()
	
	conn.close()
		
	output = money * data
	
	if print_result:
		print(f'{money}{curr1} -> {output}{curr2}')
	return output

@cache
def _convert_curr(
	money: float,
	curr1: str,
	curr2: str
	) -> float | None:
		
		try:
			url = f'https://api.frankfurter.dev/v2/rate/{curr1}/{curr2}'
			response = requests.get(url)
			response.raise_for_status()
			
			data = response.json()['rate']
			output = money * data
		except requests.RequestException:
			return None
		
		return output
			
def cached_convert_curr(
	money: float,
	curr1: str,
	curr2: str,
	print_result: bool = True
	) -> float | None:
		
		curr1 = curr1.upper()
		curr2 = curr2.upper()
		
		output = _convert_curr(money, curr1, curr2)
		
		if print_result:
			print(f'{money}{curr1} -> {output}{curr2}')
		return output