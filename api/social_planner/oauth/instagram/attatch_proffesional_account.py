from typing import  Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def attach_instagram_professional_account(
    headers: dict[str, str],
    location_id: str,
    account_id: str,
    origin_id: str,
    name: str,
    avatar: str,
    page_id: str,
    company_id: str
) -> dict[str, Any]:
    url = f"{API_BASE_URL}/social-media-posting/oauth/{location_id}/instagram/accounts/{account_id}"

    if not headers.get("Authorization") or not headers["Authorization"].startswith("Bearer "):
        raise ValueError("Missing or invalid Authorization header. Must be in format: 'Bearer {token}'")

    request_headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Version": headers.get("Version", API_VERSION),
        **headers
    }

    data = {
        "originId": origin_id,
        "name": name,
        "avatar": avatar,
        "pageId": page_id,
        "companyId": company_id
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=request_headers, json=data)
        response.raise_for_status()
        return response.json()