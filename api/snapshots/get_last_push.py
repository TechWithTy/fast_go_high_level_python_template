import httpx
from typing import  Any

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_last_snapshot_push(
    headers: dict[str, str],
    location_id: str,
    snapshot_id: str,
    company_id: str
) -> dict[str, Any]:
    """
    Get Latest Snapshot Push Status for a location id.

    Args:
        headers (dict[str, str]): The headers containing the authorization token.
        location_id (str): The ID of the location.
        snapshot_id (str): The ID of the snapshot.
        company_id (str): The ID of the company.

    Returns:
        dict[str, Any]: The API response containing snapshot push status.

    Raises:
        httpx.HTTPStatusError: If the API request fails.
        Exception: If the Authorization header is missing or invalid.
    """
    if not headers.get("Authorization") or not headers["Authorization"].startswith("Bearer "):
        raise Exception("Missing or invalid Authorization header. Must be in format: 'Bearer {token}'")

    url = f"{API_BASE_URL}/snapshots/snapshot-status/{snapshot_id}/location/{location_id}"

    request_headers = {
        "Authorization": headers["Authorization"],
        "Version": headers.get("Version", API_VERSION),
        "Accept": "application/json"
    }

    params = {"companyId": company_id}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=request_headers, params=params)
        response.raise_for_status()
        return response.json()