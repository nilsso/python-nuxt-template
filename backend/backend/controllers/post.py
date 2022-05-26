# pylama:ignore=D100,D101,D102,D103,D104,D106,D107
from typing import Type, cast

from prisma import models, types

from backend.utils.prisma_utils import OrderByInputT
from backend.utils.route_utils import PrismaTypes, prisma_controller

PostController = prisma_controller(
    models.Post,
    PrismaTypes(
        types.PostCreateInput,
        types.PostCreateWithoutRelationsInput,
        types.PostWhereUniqueInput,
        types.PostWhereInput,
        types.PostInclude,
        types.PostUpdateInput,
        types.PostUpdateManyMutationInput,
        types.PostUpsertInput,
        cast(
            Type[OrderByInputT],
            types.PostOrderByInput,
        ),
    ),
)
