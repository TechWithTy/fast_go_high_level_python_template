from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"


async def create_sub_account(
    headers: Dict[str, str], data: Dict[str, Any], api_version: str = "2021-07-28"
) -> Dict[str, Any]:
    """
    Create a Sub-Account (Formerly Location) based on the data provided.

    Args:
        headers (Dict[str, str]): Headers containing the authorization token.
        data (Dict[str, Any]): The data to create the sub-account with.
        api_version (str, optional): The API version to use. Defaults to "2021-07-28".

    Returns:
        Dict[str, Any]: The response from the API containing the created sub-account information.

    Raises:
        ValueError: If the Authorization header is missing or invalid.
        httpx.HTTPStatusError: If the API request fails.
    """
    url = f"{API_BASE_URL}/locations"

    if "Authorization" not in headers or not headers["Authorization"].startswith(
        "Bearer "
    ):
        raise ValueError("Missing or invalid Authorization header")

    request_headers = {
        "Authorization": headers["Authorization"],
        "Version": api_version,
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    logging.info(f"Creating new sub-account with name: {data.get('name', 'Unknown')}")

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, headers=request_headers)
        response.raise_for_status()
        return response.json()
