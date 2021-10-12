import pytest
from httpx import AsyncClient

from . import main


@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient(app=main.app, base_url="http://test") as client:
        response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"id": 1}
