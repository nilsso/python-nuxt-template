# pylama:ignore=D100,D101,D102,D103,D104,D106,D107
from starlette import status
from starlite import CORSConfig, Redirect, Starlite, get

from . import prisma
from .controllers import FileController, PostController, TagController, UserController

# TODO: bug report for byte (Base64 in Prisma) fields not being starlite serializable


@get(
    status_code=status.HTTP_307_TEMPORARY_REDIRECT,
    description="Redirect root to /schema",
)
def root_to_docs() -> Redirect:
    return Redirect(path="/schema")


app = Starlite(
    debug=True,
    cors_config=CORSConfig(),
    on_startup=[
        lambda: prisma.connect(),
    ],
    on_shutdown=[lambda: prisma.disconnect()],
    route_handlers=[
        root_to_docs,
        UserController,
        PostController,
        TagController,
        FileController,
    ],
)
