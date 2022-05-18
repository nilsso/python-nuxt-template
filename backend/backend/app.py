# pylama:ignore=D100,D101,D102,D103,D104,D106,D107
from copy import copy
from typing import Any

from prisma import models
from starlite import Controller, CORSConfig, OpenAPIConfig, Starlite, get

from . import prisma
from .controllers import PostController, TagController, UserController


async def init():
    await prisma.post.delete_many()
    await prisma.tag.delete_many()
    await prisma.user.delete_many()

    await prisma.user.create(
        data={
            "name": "Robert",
        },
    )
    user = await prisma.user.create(
        data={
            "name": "Nils",
        },
    )
    tag = await prisma.tag.create(
        data={
            "tag": "Generic",
        },
    )
    await prisma.post.create(
        data={
            "title": "A Post",
            "user": {
                "connect": {
                    "id": user.id,
                },
            },
            "tags": {
                "connect": {
                    "tag": tag.tag,
                },
            },
        },
    )


app = Starlite(
    debug=True,
    openapi_config=OpenAPIConfig(
        title="My API",
        version="0.0.1",
        # create_examples=True,
    ),
    cors_config=CORSConfig(
        allow_origins=["*"],
        allow_methods=["*"],
    ),
    on_startup=[
        lambda: prisma.connect(),
        init,
    ],
    on_shutdown=[lambda: prisma.disconnect()],
    route_handlers=[
        UserController,
        PostController,
        TagController,
    ],
)
