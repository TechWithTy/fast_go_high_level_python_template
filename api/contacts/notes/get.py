from typing import  Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_note(
    contact_id: str,
    note_id: str,
    headers: dict[str, str]
) -> dict[str, Any]:
    """
    Get a note for a specific contact from the Go High Level API.
    
    Args:
        contact_id: The ID of the contact
        note_id: The ID of the note to retrieve
        headers: Dictionary containing Authorization and Version headers
        
    Returns:
        Dictionary containing the note data
        
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
    
    logging.info(f"Making request to get note {note_id} for contact: {contact_id}")
    
    try:
        # Make the API request to get note
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(
                f"{API_BASE_URL}/contacts/{contact_id}/notes/{note_id}",
                headers=request_headers
            )
            
        # Handle the API response
        if response.status_code != 200:
            error_detail = response.text
            logging.error(f"API request failed with status {response.status_code}: {error_detail}")
            raise Exception(f"API request failed with status {response.status_code}: {error_detail}")
            
        return response.json()
    
    except Exception as e:
        logging.error(f"Error getting note: {str(e)}")
        raise