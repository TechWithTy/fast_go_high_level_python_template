from typing import  Any
import httpx
import logging

async def get_calendar(
    calendar_id: str,
    headers: dict[str, str]
) -> dict[str, Any]:
    """
    Get calendar by ID from the Go High Level API.
    
    Args:
        calendar_id: The ID of the calendar to retrieve
        headers: Dictionary containing Authorization and Version headers
        
    Returns:
        Dictionary containing the calendar data
        
    Raises:
        Exception: If the API request fails or if required headers are missing
    """
    # Define API base URL
    API_BASE_URL = "https://services.leadconnectorhq.com"
    
    # Validate required headers
    if not headers.get("Authorization") or not headers["Authorization"].startswith("Bearer "):
        raise Exception("Missing or invalid Authorization header. Must be in format: 'Bearer {token}'")

    if not headers.get("Version"):
        # Set default version if not provided
        headers["Version"] = "2021-04-15"
    
    # Prepare request headers
    request_headers = {
        "Authorization": headers["Authorization"],
        "Version": headers["Version"],
        "Accept": "application/json"
    }
    
    logging.info(f"Making request to get calendar: {calendar_id}")
    
    try:
        # Make the API request to get calendar
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(
                f"{API_BASE_URL}/calendars/{calendar_id}",
                headers=request_headers
            )
            
        # Handle the API response
        if response.status_code != 200:
            error_detail = response.text
            logging.error(f"API request failed with status {response.status_code}: {error_detail}")
            raise Exception(f"API request failed with status {response.status_code}: {error_detail}")
            
        return response.json()
        
    except Exception as e:
        logging.error(f"Error getting calendar: {str(e)}")
        raise