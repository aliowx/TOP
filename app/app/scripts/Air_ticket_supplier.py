import httpx

SOURCE_A_URL = ""
SOURCE_B_URL = ""

async def fetch_flights_from_source(url: str, params: dict)-> list[dict]:
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        return response.json()
    