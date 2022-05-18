# pylama:ignore=D100,D101,D102,D103,D104,D106,D107
import json
from typing import Optional

from prisma import models, types
from pydantic import BaseModel
from starlite import Body, Controller, delete, post

from backend import prisma

from .config import Config

# from getpass import getuser
# from random import shuffle


class UserFindManyArgs(BaseModel):
    __config__ = Config

    take: Optional[int]
    skip: Optional[int]
    include: Optional[types.UserInclude] = {}


UserFindManyArgs.update_forward_refs()


class UserController(Controller):
    path = "/user"
    tags = ["user"]

    @post()
    async def find_user_many(self, data: UserFindManyArgs) -> list[models.User]:
        kwargs = dict(data)
        print("kwargs", json.dumps(kwargs, indent=2, default=str))
        res = await prisma.user.find_many(**kwargs)
        print("res", json.dumps(res, indent=2, default=str))
        return res

    # @post(path="/next")
    # async def create_user_next(self) -> models.User:
    #     i = await prisma.user.count()
    #     return await prisma.user.create(data={"name": f"{getuser()} {i}"})
    #
    # @delete(path="/random")
    # async def delete_user_random(self) -> models.User | None:
    #     ids = [user.id for user in await prisma.user.find_many()]
    #     if ids:
    #         shuffle(ids)
    #         id = ids.pop()
    #         return await prisma.user.delete(where={"id": id})
    #
    # @delete(path="/all")
    # async def delete_user_all(self) -> int:
    #     return await prisma.user.delete_many()
