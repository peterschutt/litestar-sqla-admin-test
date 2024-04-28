from litestar import Litestar
from sqladmin import ModelView
from sqladmin_litestar_plugin import SQLAdminPlugin
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base


engine = create_async_engine("sqlite+aiosqlite:///example.db")
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.name]


async def on_startup() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)  # Create tables


admin = SQLAdminPlugin(views=[UserAdmin], engine=engine)
app = Litestar(plugins=[admin], on_startup=[on_startup])
