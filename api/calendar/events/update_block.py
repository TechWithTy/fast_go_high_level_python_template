import logging
from typing import Any

import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-04-15"


async def update_block_slot(
    event_id: str, block_data: dict[str, Any], headers: dict[str, str]
) -> dict[str, Any]:
    """
    Update a block slot in a calendar in Go High Level.

    Args:
        event_id: The ID of the block slot to update
        block_data: Dictionary containing block slot details (calendarId, startTime,
                   endTime, title, assignedUserId)
        headers: Dictionary containing Authorization and Version headers

    Returns:
        Dictionary containing the updated block slot data

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

    logging.info(f"Updating block slot with ID: {event_id}")

    try:
        # Make the API request to update block slot
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.put(
                f"{API_BASE_URL}/calendars/events/block-slots/{event_id}",
                headers=request_headers,
                json=block_data,
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
        logging.error(f"Error updating block slot: {str(e)}")
        raise
