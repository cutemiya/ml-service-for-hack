import typing

import psycopg2
from fastapi import APIRouter
from pydantic import BaseModel

from data.generate_and_analyze_cvs import get_all_statistics_by_user_tags, get_analyze_events
from repository.reposiotry import Repository
from service.service import Service
from utils.beatify import beatify_dict

base_router = APIRouter()

from utils.base import dbname, user, password, host, port

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cur = conn.cursor()

repository = Repository(cur)
service: Service = Service(repository)


class Item(BaseModel):
    tags: typing.List[str]


@base_router.post("/tags")
def analyze_by_tags(item: Item):
    return service.get_analyze_by_tags(item.tags)


@base_router.get("/tags/all/stat")
def analyze_all():
    return get_all_statistics_by_user_tags()


@base_router.get("/events/{account_id}")
def get_all_events(account_id: int):
    return get_analyze_events(account_id)
