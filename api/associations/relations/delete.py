from typing import  Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def delete_relation(
    relation_id: str,
    location_id: str,
    headers: dict[str, str]
) -> dict[str, Any]:
    """
    Delete an association relation by ID.
    
    Args:
        relation_id: The ID of the relation to delete
        location_id: The location ID (Sub Account ID)
        headers: Dictionary containing Authorization and Version headers
        
    Returns:
        Dictionary containing deletion status and relation details
        
    Raises:
        Exception: If the API request fails or if required headers are missing
    """
    # Validate required headers
    if not headers.get("Authorization") or not headers["Authorization"].startswith("Bearer "):
        raise Exception("Missing or invalid Authorization header. Must be in format: 'Bearer {token}'")

    if not headers.get("Version"):
        # Set default version if not provided
        headers["Version"] = API_VERSION
    
    # Prepare request headers
    request_headers = {
        "Authorization": headers["Authorization"],
        "Version": headers["Version"],
        "Accept": "application/json"
    }
    
    # Prepare query parameters
    params = {
        "locationId": location_id
    }
    
    logging.info(f"Making request to delete relation: {relation_id}")
    
    try:
        # Make the API request to delete the relation
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.delete(
                f"{API_BASE_URL}/associations/relations/{relation_id}",
                params=params,
                headers=request_headers
            )
            
            if response.status_code != 200:
                error_message = response.text
                logging.error(f"Failed to delete relation: {error_message}")
                raise Exception(f"Failed to delete relation: {error_message}")
            
            return response.json()
    except Exception as e:
        logging.error(f"Error deleting relation: {str(e)}")
        raise