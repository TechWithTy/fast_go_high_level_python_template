from typing import  Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def delete_custom_value(
    location_id: str,
    custom_value_id: str,
    headers: dict[str, str]
) -> dict[str, Any]:
    """
    Delete a custom value for a specific location.

    Args:
        location_id: The ID of the location
        custom_value_id: The ID of the custom value to delete
        headers: Dictionary containing Authorization and Version headers

    Returns:
        dict containing the API response

    Raises:
        Exception: If the API request fails or if required headers are missing
    """
    url = f"{API_BASE_URL}/locations/{location_id}/customValues/{custom_value_id}"

    if not headers.get("Authorization") or not headers["Authorization"].startswith("Bearer "):
        raise ValueError("Missing or invalid Authorization header. Must be in format: 'Bearer {token}'")

    if not headers.get("Version"):
        headers["Version"] = API_VERSION

    request_headers = {
        "Authorization": headers["Authorization"],
        "Version": headers["Version"],
        "Accept": "application/json"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(url, headers=request_headers)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise