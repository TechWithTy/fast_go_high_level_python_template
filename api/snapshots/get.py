from typing , Any, list
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_snapshots(headers: dict[str, str], company_id: str) -> list[dict[str, Any]]:
    """
    Get a list of all own and imported Snapshots.

    Args:
        headers (dict[str, str]): The headers containing the authorization token.
        company_id (str): The company ID.

    Returns:
        list[dict[str, Any]]: A list of snapshot dictionaries.

    Raises:
        httpx.HTTPStatusError: If the API request fails.
        ValueError: If the Authorization header is missing or invalid.
    """
    url = f"{API_BASE_URL}/snapshots/"
    
    if "Authorization" not in headers or not headers["Authorization"].startswith("Bearer "):
        raise ValueError("Missing or invalid Authorization header")

    request_headers = {
        "Accept": "application/json",
        "Authorization": headers["Authorization"],
        "Version": headers.get("Version", API_VERSION)
    }
    
    params = {
        "companyId": company_id
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=request_headers, params=params)
        response.raise_for_status()
        return response.json()["snapshots"]