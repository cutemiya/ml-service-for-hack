# import psycopg2 as psycopg2
# import csv
#
# from data.generate_cvs import Generator
# from repository.migrations.run import run
# from repository.reposiotry import Repository
#
# conn = psycopg2.connect(dbname='production', user='postgres', password='root', host='localhost', port=5431)
# run(conn)
#
# cur = conn.cursor()
# # cur.execute('select * from usertags group by id')
# #
# # def aaa(aa):
# #     for i in aa:
# #
# # print(cur.fetchall())
#
# gen = Generator(conn)
# gen.generate_user_tags()
# gen.analyze_by_tags()
# # print( gen.get_all_statistics_by_user_tags())
#
# import psycopg2
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# from api.handler.analyze import init
from api.server import main_router
from repository.reposiotry import Repository
from service.service import Service

# conn = psycopg2.connect(dbname='production', user='postgres', password='root', host='localhost', port=5431)
# run(conn)
#
# cur = conn.cursor()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_router)
