from typing , Any, list, Optional
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def upsert_contact(
    headers: dict[str, str],
    location_id: str,
    first_name: str | None,
    last_name: str | None,
    name: str | None,
    email: str | None,
    gender: str | None,
    phone: str | None,
    address1: str | None,
    city: str | None,
    state: str | None,
    postal_code: str | None,
    website: str | None,
    timezone: str | None,
    dnd: Optional[bool] = None,
    dnd_settings: dict[str, Any] = None,
    inbound_dnd_settings: dict[str, Any] = None,
    tags: list[str] | None = None,
    custom_fields: Optional[list[dict[str, str]]] = None,
    source: str | None,
    country: str | None,
    company_name: str | None,
    assigned_to: str | None,
) -> dict[str, Any]:
    """
    Upsert a contact in Go High Level.
    
    If Allow Duplicate Contact is disabled under Settings, the global unique identifier 
    will be used for de-duplication. If the setting is enabled, a new contact will 
    get created with the shared details.
    """
    url = f"{API_BASE_URL}/contacts/upsert"
    
    if not headers.get("Authorization") or not headers["Authorization"].startswith("Bearer "):
        raise ValueError("Missing or invalid Authorization header. Must be in format: 'Bearer {token}'")

    if not headers.get("Version"):
        headers["Version"] = API_VERSION

    request_headers = {
        "Authorization": headers["Authorization"],
        "Version": headers["Version"],
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    payload = {
        "locationId": location_id
    }
    
    optional_fields = {
        "firstName": first_name,
        "lastName": last_name,
        "name": name,
        "email": email,
        "gender": gender,
        "phone": phone,
        "address1": address1,
        "city": city,
        "state": state,
        "postalCode": postal_code,
        "website": website,
        "timezone": timezone,
        "dnd": dnd,
        "dndSettings": dnd_settings,
        "inboundDndSettings": inbound_dnd_settings,
        "tags": tags,
        "customFields": custom_fields,
        "source": source,
        "country": country,
        "companyName": company_name,
        "assignedTo": assigned_to
    }
    
    payload.update({k: v for k, v in optional_fields.items() if v is not None})
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=request_headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise