import asyncio

from sqlalchemy import Column, Integer, String
from sqlalchemy import update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

engine = create_async_engine("postgresql+asyncpg://test:test@localhost/test")
session_factory = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
session = session_factory()


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, index=True)


async def create_user():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    user = User(email="test@example.org")
    session.add(user)
    await session.commit()
    await session.refresh(user)

    query = (
        update(User)
        .where(User.id == user.id)
        .values({"email": "test2@example.org"})
        .execution_options(synchronize_session="fetch")
    )
    await session.execute(query)
    return user
