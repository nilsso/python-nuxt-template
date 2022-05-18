# pylama:ignore=D100,D101,D102,D103,D104,D106,D107
import json
from typing import Optional

from prisma import models, types
from pydantic import BaseModel
from starlite import Controller, post

from backend import prisma

from .config import Config


class TagFindManyArgs(BaseModel):
    __config__ = Config

    take: Optional[int]
    skip: Optional[int]
    include: Optional[types.TagInclude] = {}


class TagController(Controller):
    path = "/tag"
    tags = ["tag"]

    @post()
    async def find_tag_many(self, data: TagFindManyArgs) -> list[models.Tag]:
        kwargs = dict(data)
        print(json.dumps(kwargs, indent=2, default=str))
        res = await prisma.tag.find_many(**kwargs)
        print(json.dumps(res, indent=2, default=str))
        return res
