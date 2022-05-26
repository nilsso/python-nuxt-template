"""Starlite route utilities."""
from typing import Any, Optional, Type

from pydantic import create_model
from starlite import Controller, delete, get, post, put

from .prisma_utils import ModelProtocol, PrismaTypes


def prisma_controller(
    model: Type[ModelProtocol],
    prisma_types: PrismaTypes,
) -> Type[Controller]:
    """Create a Prisma model controller."""
    name = model.__name__

    CreateParams = create_model(
        f"{name}CreateParams",
        data=(prisma_types.create_input, ...),
        include=(Optional[prisma_types.include], None),
    )

    CreateManyParams = create_model(
        f"{name}CreateManyParams",
        data=(list[prisma_types.create_input], ...),
        skip_duplicates=(Optional[bool], False),
    )

    FindUniqueParams = create_model(
        f"{name}FindUniqueParams",
        where=(prisma_types.where_unique_input, ...),
        include=(Optional[prisma_types.include], None),
    )

    FindManyParams = create_model(
        f"{name}FindManyParams",
        take=(Optional[int], None),
        skip=(Optional[int], None),
        where=(Optional[prisma_types.where_input], None),
        cursor=(Optional[prisma_types.where_unique_input], None),
        include=(Optional[prisma_types.include], None),
        order=(Optional[prisma_types.order_by_input], None),
    )

    FindFirstParams = create_model(
        f"{name}FindFirstParams",
        skip=(Optional[int], None),
        where=(Optional[prisma_types.where_input], None),
        cursor=(Optional[prisma_types.where_unique_input], None),
        include=(Optional[prisma_types.include], None),
        order=(Optional[prisma_types.order_by_input], None),
    )

    DeleteParams = create_model(
        f"{name}DeleteParams",
        where=(prisma_types.where_unique_input, ...),
        include=(Optional[prisma_types.include], None),
    )

    DeleteManyParams = create_model(
        f"{name}DeleteManyParams",
        where=(prisma_types.where_input, ...),
    )

    UpdateParams = create_model(
        f"{name}UpdateParams",
        data=(prisma_types.update_input, ...),
        where=(prisma_types.where_unique_input, ...),
        include=(Optional[prisma_types.include], None),
    )

    UpdateManyParams = create_model(
        f"{name}UpdateManyParams",
        data=(prisma_types.update_many_mutation_input, ...),
        where=(prisma_types.where_input, ...),
    )

    UpsertParams = create_model(
        f"{name}UpsertParams",
        where=(prisma_types.where_unique_input, ...),
        data=(prisma_types.upsert_input, ...),
        include=(Optional[prisma_types.include], None),
    )

    QueryFirstParams = create_model(
        f"{name}QueryFirstParams",
        query=(str, ...),
        args=(Any, ...),
    )

    QueryRawParams = create_model(
        f"{name}QueryRawParams",
        query=(str, ...),
        args=(Any, ...),
    )

    class _Controller(Controller):
        __name__ = f"{name}Controller"

        path = name.lower()
        tags = [name]

        # ------------------------------------------------------------------------------------------
        # GET actions.find_many
        # ------------------------------------------------------------------------------------------
        @get(
            summary="Get Many",
            description=f"""\
Find multiple {name} records.

An empty list is returned if no records could be found.

Equivalent to `/{name.lower()}/find_many` but as a GET request and without query parameters.
            """,
        )
        async def get_many(self) -> list[model]:
            return await model.prisma().find_many()

        # ------------------------------------------------------------------------------------------
        # PUT actions.create
        # ------------------------------------------------------------------------------------------
        @put(
            path="/create",
            summary="Create",
            description=f"Create a new {name} record.",
        )
        async def prisma_create(self, data: CreateParams) -> model:
            return await model.prisma().create(**dict(data))

        # ------------------------------------------------------------------------------------------
        # PUT actions.create_many
        # ------------------------------------------------------------------------------------------
        @put(
            path="/create_many",
            summary="Create Many",
            description=f"""\
Create multiple {name} records at once.

This function is *not* available when  using SQLite.
            """,
        )
        async def prisma_create_many(self, data: CreateManyParams) -> int:
            return await model.prisma().create_many(**dict(data))

        # ------------------------------------------------------------------------------------------
        # POST actions.find_unique
        # ------------------------------------------------------------------------------------------
        @post(
            path="/find_unique",
            summary="Find Unique",
            description=f"Find a unique {name} record.",
        )
        async def prisma_find_unique(self, data: FindUniqueParams) -> Optional[model]:
            return await model.prisma().find_unique(**dict(data))

        # ------------------------------------------------------------------------------------------
        # POST actions.find_many
        # ------------------------------------------------------------------------------------------
        @post(
            path="/find_many",
            summary="Find Many",
            description=f"""\
Find multiple {name} records.

An empty list is returned if no records could be found.
            """,
        )
        async def prisma_find_many(self, data: FindManyParams) -> list[model]:
            return await model.prisma().find_many(**dict(data))

        # ------------------------------------------------------------------------------------------
        # POST actions.find_first
        # ------------------------------------------------------------------------------------------
        @post(
            path="/find_first",
            summary="Find First",
            description=f"Find a single {name} record.",
        )
        async def prisma_find_first(self, data: FindFirstParams) -> Optional[model]:
            return await model.prisma().find_first(**dict(data))

        # ------------------------------------------------------------------------------------------
        # DELETE actions.delete
        # ------------------------------------------------------------------------------------------
        @delete(
            path="/delete",
            summary="Delete",
            description=f"Delete a single {name} record.",
        )
        async def prisma_delete(self, data: DeleteParams) -> Optional[model]:
            return await model.prisma().delete(**dict(data))

        # ------------------------------------------------------------------------------------------
        # DELETE actions.delete_many
        # ------------------------------------------------------------------------------------------
        @delete(
            path="/delete_many",
            summary="Delete Many",
            description=f"Delete multiple {name} records.",
        )
        async def prisma_delete_many(self, data: DeleteManyParams) -> int:
            return await model.prisma().delete_many(**dict(data))

        # ------------------------------------------------------------------------------------------
        # PUT actions.update
        # ------------------------------------------------------------------------------------------
        @put(
            path="/update",
            summary="Update",
            description=f"Update a single {name} record.",
        )
        async def prisma_update(self, data: UpdateParams) -> Optional[model]:
            return await model.prisma().update(**dict(data))

        # ------------------------------------------------------------------------------------------
        # PUT actions.update_many
        # ------------------------------------------------------------------------------------------
        @put(
            path="/update_many",
            summary="Update Many",
            description=f"Update multiple {name} records.",
        )
        async def prisma_update_many(self, data: UpdateManyParams) -> int:
            return await model.prisma().update_many(**dict(data))

        # ------------------------------------------------------------------------------------------
        # PUT actions.upsert
        # ------------------------------------------------------------------------------------------
        @put(
            path="/upsert",
            summary="Upsert",
            description=f"Updates an existing {name} record or creates a new one.",
        )
        async def prisma_upsert(self, data: UpsertParams) -> model:
            return await model.prisma().upsert(**dict(data))

        # ------------------------------------------------------------------------------------------
        # POST actions.query_first
        # ------------------------------------------------------------------------------------------
        @post(
            path="/query_first",
            summary="Query First",
            description=f"Execute a raw SQL query, returning the first {name} result.",
        )
        async def prisma_query_first(self, data: QueryFirstParams) -> Optional[model]:
            return await model.prisma().query_first(**dict(data))

        # ------------------------------------------------------------------------------------------
        # POST actions.query_raw
        # ------------------------------------------------------------------------------------------
        @post(
            path="/query_raw",
            summary="Query Raw",
            description="Execute a raw SQL query.",
        )
        async def prisma_query_raw(self, data: QueryRawParams) -> list[model]:
            return await model.prisma().query_raw(**dict(data))

    return _Controller
