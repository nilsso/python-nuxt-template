# pylama:ignore=D100,D101,D102,D103,D104,D106,D107
from typing import Type, cast

from prisma import models, types

from backend.utils.prisma_utils import OrderByInputT
from backend.utils.route_utils import PrismaTypes, prisma_controller

UserController = prisma_controller(
    models.User,
    PrismaTypes(
        types.UserCreateInput,
        types.UserCreateWithoutRelationsInput,
        types.UserWhereUniqueInput,
        types.UserWhereInput,
        types.UserInclude,
        types.UserUpdateInput,
        types.UserUpdateManyMutationInput,
        types.UserUpsertInput,
        cast(
            Type[OrderByInputT],
            types.UserOrderByInput,
        ),
    ),
)
