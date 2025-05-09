from typing , Any, Optional
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def search_users(
    access_token: str,
    company_id: str,
    enabled_2way_sync: Optional[bool] = None,
    ids: list[str] | None = None,
    limit: int = 25,
    location_id: str | None,
    query: str | None,
    role: str | None,
    skip: int = 0,
    sort: str | None,
    sort_direction: str | None,
    user_type: str | None
) -> dict[str, Any]:
    url = f"{API_BASE_URL}/users/search"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    params = {
        "companyId": company_id,
        "enabled2waySync": enabled_2way_sync,
        "ids": ",".join(ids) if ids else None,
        "limit": limit,
        "locationId": location_id,
        "query": query,
        "role": role,
        "skip": skip,
        "sort": sort,
        "sortDirection": sort_direction,
        "type": user_type
    }

    params = {k: v for k, v in params.items() if v is not None}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()