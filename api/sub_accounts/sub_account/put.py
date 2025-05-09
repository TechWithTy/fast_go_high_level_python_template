from typing , Any
import httpx
import json

async def update_sub_account(
    location_id: str,
    headers: dict[str, str],
    sub_account_data: dict[str, Any]
) -> dict[str, Any]:
    """
    Update a Sub-Account (Formerly Location) based on the data provided.

    Args:
        location_id (str): The ID of the location to update.
        headers (dict[str, str]): Headers containing Authorization and Version.
        sub_account_data (dict[str, Any]): The data to update the sub-account with.

    Returns:
        dict[str, Any]: The updated sub-account data.

    Raises:
        httpx.HTTPStatusError: If the API request fails.
        ValueError: If required headers are missing.
    """
    url = f"https://services.leadconnectorhq.com/locations/{location_id}"
    
    if "Authorization" not in headers or not headers["Authorization"].startswith("Bearer "):
        raise ValueError("Missing or invalid Authorization header")
    
    if "Version" not in headers:
        headers["Version"] = "2021-07-28"
    
    headers.update({
        "Accept": "application/json",
        "Content-Type": "application/json"
    })

    async with httpx.AsyncClient() as client:
        response = await client.put(url, headers=headers, json=sub_account_data)
        response.raise_for_status()
        return response.json()