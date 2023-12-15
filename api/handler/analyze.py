import typing

import psycopg2
from fastapi import APIRouter
from pydantic import BaseModel

from repository.reposiotry import Repository
from service.service import Service

base_router = APIRouter()

conn = psycopg2.connect(dbname='production', user='postgres', password='root', host='localhost', port=5431)
cur = conn.cursor()

repository = Repository(cur)
service: Service = Service(repository)


class Item(BaseModel):
    tags: typing.List[str]


@base_router.post("/tags")
def analyze_by_tags(item: Item):
    return service.get_analyze_by_tags(item.tags)
