"""uvicorn app."""
from getpass import getuser
from random import shuffle

from prisma import Prisma, models
from starlite import CORSConfig, Starlite, get, post

prisma = Prisma(auto_register=True)

cors_config = CORSConfig(allow_origins=["*"])


@get(path="/")
async def index() -> str:
    """Index page."""
    return "Hello, world"


@get(path="/user/find/many")
async def user_find_many() -> list[models.User]:
    """Find many users."""
    return await prisma.user.find_many()


@post(path="/user/create/next")
async def user_create_next() -> models.User:
    """Create next user."""
    i = await prisma.user.count()
    return await prisma.user.create(data={"name": f"{getuser()} {i}"})


@post(path="/user/delete/random")
async def user_delete_random() -> models.User | None:
    """Delete random user."""
    ids = [user.id for user in await prisma.user.find_many()]
    if ids:
        shuffle(ids)
        id = ids.pop()
        return await prisma.user.delete(where={"id": id})


@post(path="/user/delete/all")
async def user_delete_all() -> None:
    """Delete all users."""
    await prisma.user.delete_many()


app = Starlite(
    cors_config=cors_config,
    on_startup=[
        lambda: prisma.connect(),
    ],
    on_shutdown=[lambda: prisma.disconnect()],
    route_handlers=[
        index,
        user_create_next,
        user_find_many,
        user_delete_random,
        user_delete_all,
    ],
)
