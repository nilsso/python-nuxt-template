# pylama:ignore=D100,D101,D102,D103,D104,D106,D107
import json
from typing import Optional

from prisma import models, types
from pydantic import BaseModel
from starlite import Controller, post

from backend import prisma

from .config import Config


class PostFindManyArgs(BaseModel):
    __config__ = Config

    take: Optional[int]
    skip: Optional[int]
    include: Optional[types.PostInclude] = {}


class PostController(Controller):
    path = "/post"
    tags = ["post"]

    @post()
    async def find_post_many(self, data: PostFindManyArgs) -> list[models.Post]:
        kwargs = dict(data)
        print(json.dumps(kwargs, indent=2, default=str))
        res = await prisma.post.find_many(**kwargs)
        print(json.dumps(res, indent=2, default=str))
        return res
