from typing import List

import psycopg2

conn = psycopg2.connect(dbname='production', user='postgres', password='root', host='localhost', port=5431)
cur = conn.cursor()


def beatify_first_analyze(data: List[tuple]):
    return_data = dict()

    for item in data:
        cur.execute(f"select first_name, middle_name, last_name from userdetails where account_id = {item[0]}")
        response = cur.fetchone()
        name = f'{response[0]} {response[1]} {response[2]}'

        return_data[name] = {"rate": item[1], "account_id": item[0]}

    return return_data
