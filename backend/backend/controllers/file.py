# pylama:ignore=D100,D101,D102,D103,D104,D106,D107
from typing import Type, cast

from prisma import models, types

from backend.utils.prisma_utils import OrderByInputT
from backend.utils.route_utils import PrismaTypes, prisma_controller

FileController = prisma_controller(
    models.File,
    PrismaTypes(
        types.FileCreateInput,
        types.FileCreateWithoutRelationsInput,
        types.FileWhereUniqueInput,
        types.FileWhereInput,
        types.FileInclude,
        types.FileUpdateInput,
        types.FileUpdateManyMutationInput,
        types.FileUpsertInput,
        cast(
            Type[OrderByInputT],
            types.FileOrderByInput,
        ),
    ),
)
