import csv

import psycopg2
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np
import pandas as pd

from utils.base import dbname, user, password, host, port

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)


def generate_user_tags():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
            select d.account_id, t.title as tag from "UserTag" t
            right join "UserDetails" d on t.account_id = d.account_id
            """)

            with open("data/user_tags.csv", "w", newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                csv_writer.writerows(cursor)


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


def get_all_statistics_by_user_tags():
    generate_user_tags()
    df = pd.read_csv('data/user_tags.csv')
    stat = dict()
    for k, v in df.pivot_table(index=['tag'], aggfunc='size').sort_values(
            key=lambda x: (np.tan(x.cumsum()))).items():
        stat[k] = v
    return stat


def get_analyze_events(account_id: int):
    cur = conn.cursor()
    cur.execute(
        f'select e.id from "Event" e join user_events u on e.id = u.event_id where u.account_id = {account_id} and u.status = 1');
    ids = cur.fetchall()

    titles_dict, description_dict = dict(), dict()

    titles = ""
    description = ""

    for i in ids:
        cur.execute(f"select title, description from event where id={i[0]}")
        res = cur.fetchall()[0]

        titles += f" {res[0]}"
        description += f" {res[1]}"

    cur.execute('select id, title, description from event')
    all_ev = cur.fetchall()

    for item in all_ev:
        if item[0] in [i[0] for i in ids]:
            continue

        cs_title_vt = TfidfVectorizer().fit_transform([item[1], titles])
        cs_description_vt = TfidfVectorizer().fit_transform([item[2], description])

        cs_t = cosine_similarity(cs_title_vt)[0][1]
        cs_d = cosine_similarity(cs_description_vt)[0][1]

        titles_dict[item[0]] = cs_t + cs_d / 2

    return titles_dict
