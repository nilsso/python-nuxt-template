"""Python Prisma utilities."""
from typing import (
    Any,
    Mapping,
    NamedTuple,
    Optional,
    Protocol,
    Type,
    TypeAlias,
    runtime_checkable,
)

from prisma import types

CreateInputT: TypeAlias = Mapping[str, object]
CreateWithoutRelationsInputT: TypeAlias = Mapping[str, Any]
WhereInputT: TypeAlias = Mapping[str, object]
WhereUniqueInputT: TypeAlias = Mapping[str, object]
IncludeT: TypeAlias = Mapping[str, object]
UpdateInputT: TypeAlias = Mapping[str, object]
UpdateManyMutationInputT: TypeAlias = Mapping[str, object]
UpsertInputT: TypeAlias = Mapping[str, object]
OrderByInputT: TypeAlias = Mapping[str, types.SortOrder]


class PrismaTypes(NamedTuple):
    """Group of Python Prisma argument types."""

    create_input: Type[CreateInputT]
    create_without_relationsInput: Type[CreateWithoutRelationsInputT]
    where_unique_input: Type[WhereUniqueInputT]
    where_input: Type[WhereInputT]
    include: Type[IncludeT]
    update_input: Type[UpdateInputT]
    update_many_mutation_input: Type[UpdateManyMutationInputT]
    upsert_input: Type[UpsertInputT]
    order_by_input: Type[OrderByInputT]


# TODO:
# - upgrade to 3.11 and replace str with LiteralString in query_first and query_raw
@runtime_checkable
class ActionsProtocol(Protocol):
    """Python Prisma actions protocol.

    The action class must provide the following methods:
    - `create`
    - `create_many`
    - `find_unique`
    - `find_many`
    - `find_first`
    - `delete`
    - `delete_many`
    - `update`
    - `update_many`
    - `upsert`
    - `query_first`
    - `query_raw`

    But because of duck typing limitations, strict requirements on parameters could be imposed.
    """

    async def create(
        self,
        data: Any,
        include: Optional[Any] = None,
    ) -> Any:
        """Create a new record.

        Arguments:
            data: CreateInputT
                Record data
            include: Optional[IncludeT]
                Specifies which relations should be loaded on the returned model
        """
        ...

    async def create_many(
        self,
        data: list[Any],
        *,
        skip_duplicates: Optional[bool] = None,
    ) -> int:
        """Create multiple records at once.

        This function is *not* available when using SQLite.

        Arguments:
            data: list[CreateWithoutRelationsInputT]
                List of record data
            skip_duplicates: Optional[bool]
                Boolean flag for ignoring unique constraint errors
        """
        ...

    async def find_unique(
        self,
        where: Any,
        include: Optional[Any] = None,
    ) -> Optional[Any]:
        """Find a unique record.

        Arguments:
            where: WhereUniqueInputT
                Filter to find the record, must be unique
            include: Optional[IncludeT]
                Specifies which relations should be loaded on the returned model
        """
        ...

    async def find_many(
        self,
        take: Optional[int] = None,
        skip: Optional[int] = None,
        where: Optional[Any] = None,
        cursor: Optional[Any] = None,
        include: Optional[Any] = None,
        order: Optional[Any | list[Any]] = None,
    ) -> list[Any]:
        """Find multiple records.

        An empty list is returned if no records could be found.

        Arguments:
            take: Optional[int]
                Limit the maximum number of records returned
            skip: Optional[int]
                Ignore the first N results
            where: Optional[WhereInputT]
                Filter to select records
            cursor: Optional[WhereUniqueInputT]
                Specifies the position in the list to start returning results from
                (typically an ID field)
            include: Optional[IncludeT]
                Specifies which relations should be loaded on the returned model
            order: Optional[OrderByInputT | list[OrderByInputT]]
                Order the returned records by any field
        """
        ...

    async def find_first(
        self,
        skip: Optional[int] = None,
        where: Optional[Any] = None,
        cursor: Optional[Any] = None,
        include: Optional[Any] = None,
        order: Optional[Any] = None,
    ) -> Optional[Any]:
        """Find a single record.

        Arguments:
            skip: Optional[int]
                Ignore the first N records
            where: Optional[WhereInputT]
                Filter to select the record\
            cursor: Optional[WhereUniqueInputT]
                Specifies the position in the list to start returning results from
                (typically an ID field)
            include: Optional[IncludeT
                Specifies which relations should be loaded on the returned model
            order: Optional[OrderByInputT | list[OrderByInputT]]
                Order the returned records by any field
        """
        ...

    async def delete(
        self,
        where: Any,
        include: Optional[Any] = None,
    ) -> Optional[Any]:
        """Delete a single record.

        Arguments:
            where: WhereUniqueInputT
                Filter to select the record to be deleted, must be unique
            include: Optional[IncludeT]
                Specifies which relations should be loaded on the returned model
        """
        ...

    async def delete_many(
        self,
        where: Any,
    ) -> int:
        """Delete multiple records.

        Arguments:
            where: Optional[WhereInputT]
                Optional filter to find the records to be deleted
        """
        ...

    async def update(
        self,
        data: Any,
        where: Any,
        include: Optional[Any] = None,
    ) -> Optional[Any]:
        """Update a single record.

        Arguments:
            data: UpdateInputT
                Record data specifying what to update
            where: WhereUniqueInputT
                Filter to select the unique record to create/update
            include: Optional[IncludeT]
                Specifies which relations should be loaded on the returned model
        """
        ...

    async def update_many(
        self,
        data: Any,
        where: Any,
    ) -> int:
        """Update multiple records.

        Arguments:
            data: UpdateManyMutationInputT
                Data to update the selected records to
            where: WhereInputT
                Filter to select the records to update
        """
        ...

    async def upsert(
        self,
        where: Any,
        data: Any,
        include: Optional[Any] = None,
    ) -> Any:
        """Updates an existing record or create a new one.

        Arguments:
            where: WhereUniqueInputT
                Filter to select the unique record to create/update
            data: UpsertInputT
                Data specifying what fields to set on create and update/include
            include: Optional[IncludeT]
                Specifies which relations should be loaded on the returned model
        """
        ...

    async def query_first(
        self,
        query: str,
        *args: Any,
    ) -> Optional[Any]:
        """Execute a raw SQL query, returning the first result.

        Arguments:
            query: str
                The raw SQL query string to be executed
            *args: Any
                Parameters to be passed to the SQL query, these MUST be used over string formatting
                to avoid an SQL injection vulnerability
        """
        ...

    async def query_raw(
        self,
        query: str,
        *args: Any,
    ) -> list[Any]:
        """Execute a raw SQL query.

        Arguments:
            query: str
                The raw SQL query string to be executed
            *args: Any
                Parameters to be passed to the SQL query, these MUST be used over string formatting
                to avoid an SQL injection vulnerability
        """
        ...


@runtime_checkable
class ModelProtocol(Protocol):
    """Python Prisma model protocol."""

    @classmethod
    def prisma(cls) -> ActionsProtocol:
        """Get the Prisma actions for this model."""
        ...
