# pylama:ignore=D100,D101,D102,D103,D104,D106,D107

from prisma import models
from starlite import Controller, CORSConfig, Starlite, get

from . import prisma
from .controllers import UserController


class PostController(Controller):
    path = "/post"
    tags = ["post"]

    @get()
    async def find_post_many(self) -> list[models.Post]:
        return await prisma.post.find_many()


class TagController(Controller):
    path = "/tag"
    tags = ["tag"]

    @get()
    async def find_tag_many(self) -> list[models.Tag]:
        return await prisma.tag.find_many()


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
    cors_config=CORSConfig(
        allow_origins=["*"],
        allow_methods=["*"],
    ),
    on_startup=[
        lambda: prisma.connect(),
        # init,
    ],
    on_shutdown=[lambda: prisma.disconnect()],
    route_handlers=[
        UserController,
        PostController,
        TagController,
    ],
)
