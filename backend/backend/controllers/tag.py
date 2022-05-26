# pylama:ignore=D100,D101,D102,D103,D104,D106,D107
from typing import Type, cast

from prisma import models, types

from backend.utils.prisma_utils import OrderByInputT
from backend.utils.route_utils import PrismaTypes, prisma_controller

TagController = prisma_controller(
    models.Tag,
    PrismaTypes(
        types.TagCreateInput,
        types.TagCreateWithoutRelationsInput,
        types.TagWhereUniqueInput,
        types.TagWhereInput,
        types.TagInclude,
        types.TagUpdateInput,
        types.TagUpdateManyMutationInput,
        types.TagUpsertInput,
        cast(
            Type[OrderByInputT],
            types.TagOrderByInput,
        ),
    ),
)
