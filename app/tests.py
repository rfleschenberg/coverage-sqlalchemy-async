import pytest

from . import models


@pytest.mark.asyncio
async def test_create_user():
    await models.create_user()
