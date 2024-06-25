import enum
from datetime import UTC, datetime
from typing import Annotated

from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    func,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base
from .config import intpk, str_256


#
# Императивный стиль
#
class _ExampleEnumImp(enum.Enum):
    first_var = "1"
    second_var = "2"


metadata_obj = MetaData()
"""Метаданные о созданных таблицах"""


my_table = Table(
    "tablename_old",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("first_col", String(50)),
    Column(
        "enum_val",
        Enum(_ExampleEnumImp, values_callable=lambda obj: [e.value for e in obj]),
        nullable=False,
    ),
    Column("date_val", DateTime, server_default=func.now()),
)


#
# Декларативный стиль
#
class _ExampleEnumDecl(enum.Enum):
    first_var = "1"
    second_var = "2"


class ExampleTable(Base):
    __tablename__ = "tablename"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_col: Mapped[str]

    extern_conn: Mapped[list["TestTable"]] = relationship(back_populates="worker")


class ExampleTypes(Base):
    __tablename__ = "types_examples"

    id: Mapped[intpk]
    limit_val: Mapped[str | None] = mapped_column(String(50))
    maybe_none_val: Mapped[str_256 | None]
    enum_val: Mapped[_ExampleEnumDecl] = mapped_column(
        Enum(_ExampleEnumDecl, values_callable=lambda obj: [e.value for e in obj])
    )
    foreign_val: Mapped[int | None] = mapped_column(
        ForeignKey(
            "tablename.id",
            ondelete="CASCADE",
            # ondelete="SET NULL",
        )
    )
    # foreign_val: Mapped[int] = mapped_column(ForeignKey(ExampleTable.id))
    date_val: Mapped[datetime] = mapped_column(server_default=func.now())
    # date_val: Mapped[datetime] = mapped_column(
    #     server_default=text("TIMEZONE('utc',now())")
    # )
    # date_val: Mapped[datetime] = mapped_column(default=datetime.now())


class Workload(enum.Enum):
    fulltime = 1
    parttime = 2


class TestTable(Base):
    __tablename__ = "testtable"

    id: Mapped[intpk]
    title: Mapped[str_256]
    compensation: Mapped[int]
    workload: Mapped[Workload]
    worker_id: Mapped[int | None] = mapped_column(
        ForeignKey("tablename.id", ondelete="CASCADE")
    )
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    worker: Mapped["ExampleTable"] = relationship(back_populates="extern_conn")
