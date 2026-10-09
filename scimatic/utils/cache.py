"""SciMatic Caching System"""

from pathlib import Path
import os
import sys
from datetime import datetime
from typing import Callable, Any
import sqlite3
import json
from contextlib import contextmanager


def _default_path() -> Path:
    if sys.platform == 'win32':
        return Path.home() / 'Downloads'

    if sys.platform == 'android' or Path('/storage/emulated/0').exists():
        return Path('/storage/emulated/0') / 'Download'

    xdg = os.environ.get('XDG_DOWNLOAD_DIR')
    return Path(xdg) if xdg else Path.home() / 'Downloads'


PATH = _default_path()
PATH.mkdir(parents=True, exist_ok=True)


class Cache:
    """Cache function results using JSON-compatible values.

    Both backends serialize inputs and outputs as JSON. Values outside JSON's
    type model may change type when read from the cache (for example, tuples
    become lists and non-string dictionary keys become strings).
    """

    @staticmethod
    def _function_identity(func: Callable) -> str:
        return f'{func.__module__}.{func.__qualname__}'

    def __init__(self, filename: str):
        self.file = Path(filename)

        supported = {'.db', '.json', ''}

        if self.file.suffix not in supported:
            print('💥 SciMatic failed [E0001].\n')
            print('☝️ Reason: File is not a supported format.')
            print('💡 Tip: Use the following file formats:')
            print('\t.db: For large datasets.')
            print('\t.json: For small, readable data.')
            print(
                '🔗 Link: https://github.com/'
                'bingchiliingsacker-dot/SciMatic_Errors/blob/main/errors/'
                'File-Errors%5BE0001-E0100%5D/%5BE0001%5D.md'
            )
            print('')
            raise ValueError(
                'File is not a supported format. '
                'Refer to the text above for more information.'
            )

        if self.file.suffix == '':
            self.file = self.file.with_suffix('.db')

        self.location = PATH / self.file.name

        modes = {
            '.db': 0,
            '.json': 1
        }

        self.mode = modes[self.file.suffix]

        if self.mode == 0:
            with sqlite3.connect(self.location) as conn:
                cursor = conn.cursor()

                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS cache (
                        id INTEGER PRIMARY KEY,
                        function TEXT,
                        arguments TEXT,
                        keyword_arguments TEXT,
                        output TEXT,
                        ttl REAL
                    )
                    """
                )

        elif self.mode == 1:
            if not self.location.exists():
                self._write_json([])

    @contextmanager
    def _connect(self):
        conn = sqlite3.connect(self.location)
        try:
            with conn:  # commit on success, rollback on error
                yield conn
        finally:
            conn.close()  # actually release the file

    @staticmethod
    def _error_parameter(
        message: str,
        tip: str
    ) -> None:
        print('💥 SciMatic failed [E0601].')
        print('')
        print(f'☝️ Reason: {message}')
        print(f'💡 Tip: {tip}')
        print('')
        print(
            '🔗 Link: https://github.com/'
            'bingchiliingsacker-dot/SciMatic_Errors/'
            'blob/main/errors/User-Errors'
            '%5BE0601-E0800%5D/%5BE0601%5D.md'
        )
        raise ValueError(
            f'{message} '
            'Refer to the text above for more information.'
        )

    @staticmethod
    def _error_row(
        idx: int
    ) -> None:
        print('💥 SciMatic failed [E0003].')
        print('')
        print(f'☝️ Reason: Row {idx} does not exist.')
        print('💡 Tip: Create the row before accessing it.')
        print('')
        print(
            '🔗 Link: https://github.com/'
            'bingchiliingsacker-dot/SciMatic_Errors/'
            'blob/main/errors/File-Errors'
            '%5BE0001-E0100%5D/%5BE0003%5D.md'
        )
        raise ValueError(
            f'Row number {idx} does not exist. '
            'Refer to the text above for more information.'
        )

    def _write_json(self, rows: list) -> None:
        data = json.dumps(rows)  # raises here, before the real file is touched
        tmp = self.location.with_name(self.location.name + '.tmp')
        tmp.write_text(data)
        os.replace(tmp, self.location)  # atomic swap

    def cache(
        self,
        ttl: int | None = 10
    ) -> Callable:

        if ttl is None:
            self._error_parameter(
                'Required parameter `ttl` is not given.',
                'Provide a TTL value in seconds.'
            )

        def real_cache(
            func: Callable
        ) -> Callable:

            function_identity = self._function_identity(func)
            serialized_kwargs = lambda kwargs: json.dumps(
                kwargs, sort_keys=True
            )

            def wrapper(*args, **kwargs) -> Any | None:
                now = datetime.now().timestamp()

                if self.mode == 0:
                    with self._connect() as conn:
                        cursor = conn.cursor()

                        # Remove expired entries
                        cursor.execute(
                            'DELETE FROM cache WHERE ttl < ?',
                            (now,)
                        )

                        conn.commit()

                        cursor.execute(
                            """
                            SELECT * FROM cache
                            WHERE function = ?
                            AND arguments = ?
                            AND keyword_arguments = ?
                            """,
                            (
                                function_identity,
                                json.dumps(args),
                                serialized_kwargs(kwargs)
                            )
                        )

                        row = cursor.fetchone()

                        if row is None:
                            result = func(*args, **kwargs)

                            expires_at = datetime.now().timestamp() + ttl

                            cursor.execute(
                                """
                                INSERT INTO cache
                                (
                                    function,
                                    arguments,
                                    keyword_arguments,
                                    output,
                                    ttl
                                )
                                VALUES (?, ?, ?, ?, ?)
                                """,
                                (
                                    function_identity,
                                    json.dumps(args),
                                    serialized_kwargs(kwargs),
                                    json.dumps(result),
                                    expires_at
                                )
                            )

                            conn.commit()

                            return result

                        return json.loads(row[4])

                elif self.mode == 1:
                    with self.location.open() as f:
                        rows = json.load(f)

                    # Remove expired entries
                    unexpired_rows = [
                        row for row in rows
                        if row['ttl'] >= now
                    ]
                    if len(unexpired_rows) != len(rows):
                        rows = unexpired_rows
                        self._write_json(rows)
                    else:
                        rows = unexpired_rows

                    row = next(
                        (
                            row for row in rows
                            if row['function'] == function_identity
                            and row['arguments'] == json.dumps(args)
                            and row['keyword_arguments']
                            == serialized_kwargs(kwargs)
                        ),
                        None
                    )

                    if row is None:
                        result = func(*args, **kwargs)

                        if rows:
                            idx = max(
                                row['id'] for row in rows
                            ) + 1
                        else:
                            idx = 1

                        rows.append(
                            {
                                'id': idx,
                                'function': function_identity,
                                'arguments': json.dumps(args),
                                'keyword_arguments': serialized_kwargs(kwargs),
                                'output': result,
                                'ttl': datetime.now().timestamp() + ttl
                            }
                        )

                        self._write_json(rows)

                        return result

                    return row['output']

                return None

            return wrapper

        return real_cache

    def clear(
        self
    ) -> None:

        if self.mode == 0:
            with self._connect() as conn:
                cursor = conn.cursor()

                cursor.execute('DELETE FROM cache')
                conn.commit()

        elif self.mode == 1:
            self._write_json([])

    def inc_ttl(
        self,
        ttl: int | None,
        idx: int | None = None
    ) -> None:

        if ttl is None:
            self._error_parameter(
                'Required parameter `ttl` is not given.',
                'Provide a TTL value in seconds.'
            )

        if idx is None:
            self._error_parameter(
                'Required parameter `idx` is not given.',
                'Provide the `idx` parameter.'
            )

        if self.mode == 0:
            with self._connect() as conn:
                cursor = conn.cursor()

                cursor.execute(
                    'SELECT ttl FROM cache WHERE id = ?',
                    (idx,)
                )

                row = cursor.fetchone()

                if row is None:
                    self._error_row(idx)

                cursor.execute(
                    """
                    UPDATE cache
                    SET ttl = ?
                    WHERE id = ?
                    """,
                    (row[0] + ttl, idx)
                )

                conn.commit()

        elif self.mode == 1:
            with self.location.open('r') as f:
                rows = json.load(f)

            row = next(
                (
                    row for row in rows
                    if row['id'] == idx
                ),
                None
            )

            if row is None:
                self._error_row(idx)

            row['ttl'] += ttl

            self._write_json(rows)

        return None

    def exists(
        self,
        idx: int
    ) -> bool | None:

        if self.mode == 0:
            with self._connect() as conn:
                cursor = conn.cursor()

                cursor.execute(
                    'SELECT 1 FROM cache WHERE id = ?',
                    (idx,)
                )

                return cursor.fetchone() is not None

        elif self.mode == 1:
            with self.location.open() as f:
                rows = json.load(f)

            return any(
                row['id'] == idx
                for row in rows
            )

        return None

    def set(
        self,
        func: Callable,
        ttl: int | None = None,
        *args,
        **kwargs
    ) -> None:

        if ttl is None:
            self._error_parameter(
                'Required parameter `ttl` is not given.',
                'Provide a TTL value in seconds.'
            )

        now = datetime.now().timestamp()
        function_identity = self._function_identity(func)
        serialized_kwargs = json.dumps(kwargs, sort_keys=True)

        if self.mode == 0:
            with self._connect() as conn:
                cursor = conn.cursor()

                cursor.execute(
                    'DELETE FROM cache WHERE ttl < ?',
                    (now,)
                )

                cursor.execute(
                    """
                    SELECT * FROM cache
                    WHERE function = ?
                    AND arguments = ?
                    AND keyword_arguments = ?
                    """,
                    (
                        function_identity,
                        json.dumps(args),
                        serialized_kwargs
                    )
                )

                row = cursor.fetchone()

                if row is None:
                    result = func(*args, **kwargs)
                    expires_at = datetime.now().timestamp() + ttl

                    cursor.execute(
                        """
                        INSERT INTO cache
                        (
                            function,
                            arguments,
                            keyword_arguments,
                            output,
                            ttl
                        )
                        VALUES (?, ?, ?, ?, ?)
                        """,
                        (
                            function_identity,
                            json.dumps(args),
                            serialized_kwargs,
                            json.dumps(result),
                            expires_at
                        )
                    )

                    conn.commit()

            return None

        elif self.mode == 1:
            with self.location.open() as f:
                rows = json.load(f)

            rows = [
                row for row in rows
                if row['ttl'] >= now
            ]

            row = next(
                (
                    row for row in rows
                    if row['function'] == function_identity
                    and row['arguments'] == json.dumps(args)
                    and row['keyword_arguments']
                    == serialized_kwargs
                ),
                None
            )

            if row is None:
                result = func(*args, **kwargs)
                expires_at = datetime.now().timestamp() + ttl

                if rows:
                    idx = max(
                        row['id'] for row in rows
                    ) + 1
                else:
                    idx = 1

                rows.append(
                    {
                        'id': idx,
                        'function': function_identity,
                        'arguments': json.dumps(args),
                        'keyword_arguments': serialized_kwargs,
                        'output': result,
                        'ttl': expires_at
                    }
                )

                self._write_json(rows)

            return None

        return None

    def get(
        self,
        idx: int | None = None,
        print_result: bool = False
    ) -> Any | None:

        if idx is None:
            self._error_parameter(
                'Required parameter `idx` is not given.',
                'Provide an ID to retrieve a cached value.'
            )

        now = datetime.now().timestamp()

        if self.mode == 0:
            with self._connect() as conn:
                cursor = conn.cursor()

                # Remove expired entries
                cursor.execute(
                    'DELETE FROM cache WHERE ttl < ?',
                    (now,)
                )

                conn.commit()

                cursor.execute(
                    'SELECT * FROM cache WHERE id = ?',
                    (idx,)
                )

                row = cursor.fetchone()

                if row is None:
                    return None

                if print_result:
                    print(f'ID: {row[0]}')
                    print(f'Function: {row[1]}')
                    print(f'Arguments: {row[2]}')
                    print(f'Keyword Arguments: {row[3]}')
                    print(f'Output: {row[4]}')
                    print(
                        f'TTL: {max(0, row[5] - now)}'
                    )

                return json.loads(row[4])

        elif self.mode == 1:
            with self.location.open() as f:
                rows = json.load(f)

            # Remove expired entries
            valid_rows = [
                row for row in rows
                if row['ttl'] >= now
            ]

            if len(valid_rows) != len(rows):
                with self.location.open('w') as f:
                    json.dump(valid_rows, f)

            row = next(
                (
                    row for row in valid_rows
                    if row['id'] == idx
                ),
                None
            )

            if row is None:
                return None

            if print_result:
                print(f'ID: {row["id"]}')
                print(f'Function: {row["function"]}')
                print(f'Arguments: {row["arguments"]}')
                print(
                    f'Keyword Arguments: '
                    f'{row["keyword_arguments"]}'
                )
                print(f'Output: {row["output"]}')
                print(
                    f'TTL: {max(0, row["ttl"] - now)}'
                )

            return row['output']

        return None

