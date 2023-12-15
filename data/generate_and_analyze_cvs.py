import csv

import psycopg2
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np
import pandas as pd

from utils.base import dbname, user, password, host, port

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)


def generate_user_tags():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
            select d.account_id, t.title as tag from usertag t
            right join userdetails d on t.account_id = d.account_id
            """)

            with open("data/user_tags.csv", "w", newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                csv_writer.writerows(cursor)


# def generate_user_events(self):
#     with self.conn:
#         with self.conn.cursor() as cursor:
#             cursor.execute("select * from user_events")
#             with open("data/user_events.csv", "w", newline='') as csv_file:
#                 csv_writer = csv.writer(csv_file)
#                 csv_writer.writerow([i[0] for i in cursor.description])  # write headers
#                 csv_writer.writerows(cursor)


def analyze_by_tags(company_tags):
    generate_user_tags()
    cv = CountVectorizer()
    df = pd.read_csv('data/user_tags.csv')

    users = dict()
    # get company tags
    company_tags_text = " ".join(company_tags)

    for k, v in df.groupby('account_id')['tag'].apply(list).items():
        users[k] = cosine_similarity(cv.fit_transform([" ".join(v), company_tags_text]))[0][1]
    return sorted(users.items(), key=lambda x: x[1], reverse=True)


def get_all_statistics_by_user_tags(self):
    df = pd.read_csv('data/user_tags.csv')
    stat = dict()
    for k, v in df.pivot_table(index=['tag'], aggfunc='size').sort_values(
            key=lambda x: (np.tan(x.cumsum()))).items():
        stat[k] = v
    return stat
