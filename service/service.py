import typing

from data.generate_and_analyze_cvs import analyze_by_tags
from repository.reposiotry import Repository
from utils.beatify import beatify_first_analyze


class Service:
    def __init__(self, repo: Repository):
        self.repo = repo

    def get_analyze_by_tags(self, tags: typing.List[str]):
        recommendation = analyze_by_tags(tags)
        beaty = beatify_first_analyze(recommendation)
        print(beaty)
        return {"stats": beaty}
