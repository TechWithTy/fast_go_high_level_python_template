from typing import  Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def disconnect_custom_provider(headers: dict[str, str], location_id: str, live_mode: bool) -> dict[str, Any]:
    """
    Disconnect an existing payment config for a given location.

    Args:
        headers (dict[str, str]): The headers containing the authorization token.
        location_id (str): The ID of the location.
        live_mode (bool): Whether the config is for test mode or live mode.

    Returns:
        dict[str, Any]: The response data from the API.

    Raises:
        httpx.HTTPStatusError: If the API request fails.
        ValueError: If the Authorization header is missing or invalid.
    """
    url = f"{API_BASE_URL}/payments/custom-provider/disconnect"

    if "Authorization" not in headers or not headers["Authorization"].startswith("Bearer "):
        raise ValueError("Missing or invalid Authorization header")

    request_headers = {
        "Authorization": headers["Authorization"],
        "Version": API_VERSION,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    params = {
        "locationId": location_id
    }

    data = {
        "liveMode": live_mode
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=request_headers, params=params, json=data)
        response.raise_for_status()
        return response.json()