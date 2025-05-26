from typing import  Any, Optional
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_categories_by_location_id(
    headers: dict[str, str],
    location_id: str,
    limit: int | None,
    search_text: str | None,
    skip: int | None
) -> dict[str, Any]:
    url = f"{API_BASE_URL}/social-media-posting/{location_id}/categories"

    if not headers.get("Authorization") or not headers["Authorization"].startswith("Bearer "):
        raise ValueError("Missing or invalid Authorization header. Must be in format: 'Bearer {token}'")

    request_headers = {
        "Authorization": headers["Authorization"],
        "Version": headers.get("Version", API_VERSION),
        "Accept": "application/json"
    }

    params = {}
    if limit:
        params["limit"] = limit
    if search_text:
        params["searchText"] = search_text
    if skip:
        params["skip"] = skip

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=request_headers, params=params)
        response.raise_for_status()
        return response.json()