import typing

from psycopg2._psycopg import cursor


class Repository:
    def __init__(self, cur: cursor):
        self._cur = cur

    def select_all_tags(self) -> typing.List:
        try:
            self._cur.execute("select * from usertag")
            return self._cur.fetchall()
        except Exception as e:
            print(e)
            return []
