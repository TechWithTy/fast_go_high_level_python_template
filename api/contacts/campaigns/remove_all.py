from typing import  Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def remove_all_campaigns(
    contact_id: str,
    headers: dict[str, str]
) -> dict[str, bool]:
    """
    Remove a contact from every campaign in Go High Level.
    
    Args:
        contact_id: The ID of the contact
        headers: Dictionary containing Authorization and Version headers
        
    Returns:
        Dictionary containing success status
        
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
    
    logging.info(f"Making request to remove contact {contact_id} from all campaigns")
    
    try:
        # Make the API request to remove contact from all campaigns
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.delete(
                f"{API_BASE_URL}/contacts/{contact_id}/campaigns/removeAll",
                headers=request_headers
            )
            
        # Handle the API response
        if response.status_code != 200:
            error_detail = response.text
            logging.error(f"API request failed with status {response.status_code}: {error_detail}")
            raise Exception(f"API request failed with status {response.status_code}: {error_detail}")
            
        return response.json()
    
    except Exception as e:
        logging.error(f"Error removing contact from all campaigns: {str(e)}")
        raise