from typing import  Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_custom_field(location_id: str, custom_field_id: str, headers: dict[str, str]) -> dict[str, Any]:
    """
    Get a custom field from Go High Level API.

    Args:
        location_id: The ID of the location
        custom_field_id: The ID of the custom field
        headers: Dictionary containing Authorization and Version headers

    Returns:
        Dictionary containing the custom field data

    Raises:
        Exception: If the API request fails or if required headers are missing
    """
    if not headers.get("Authorization") or not headers["Authorization"].startswith("Bearer "):
        raise Exception("Missing or invalid Authorization header. Must be in format: 'Bearer {token}'")

    request_headers = {
        "Authorization": headers["Authorization"],
        "Version": headers.get("Version", API_VERSION),
        "Accept": "application/json"
    }

    url = f"{API_BASE_URL}/locations/{location_id}/customFields/{custom_field_id}"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=request_headers)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise Exception(f"Failed to get custom field: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise Exception(f"An error occurred while getting custom field: {e}")