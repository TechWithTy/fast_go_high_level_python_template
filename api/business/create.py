import logging
from typing import Any

import httpx

# Constants
API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"


async def create_business(
    business_data: dict[str, Any], headers: dict[str, str]
) -> dict[str, Any]:
    """
    Create a business in Go High Level.

    Args:
        business_data: Dictionary containing business details like name, locationId, phone, etc.
        headers: Dictionary containing Authorization and Version headers

    Returns:
        Dictionary containing the created business data

    Raises:
        Exception: If the API request fails or if required headers are missing
    """
    # Validate required headers
    if not headers.get("Authorization") or not headers["Authorization"].startswith(
        "Bearer "
    ):
        raise Exception(
            "Missing or invalid Authorization header. Must be in format: 'Bearer {token}'"
        )

    if not headers.get("Version"):
        # Set default version if not provided
        headers["Version"] = API_VERSION

    # Prepare request headers
    request_headers = {
        "Authorization": headers["Authorization"],
        "Version": headers["Version"],
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    logging.info(f"Creating business with name: {business_data.get('name', 'Unknown')}")

    try:
        # Make the API request to create business
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(
                f"{API_BASE_URL}/businesses/",
                headers=request_headers,
                json=business_data,
            )

        # Handle the API response
        if response.status_code != 201:
            error_detail = response.text
            logging.error(
                f"API request failed with status {response.status_code}: {error_detail}"
            )
            raise Exception(
                f"API request failed with status {response.status_code}: {error_detail}"
            )

        return response.json()
    except Exception as e:
        logging.error(f"Error creating business: {str(e)}")
        raise
