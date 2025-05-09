from typing , Any, Optional
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def search_opportunities(
    headers: dict[str, str],
    location_id: str,
    assigned_to: str | None,
    campaign_id: str | None,
    contact_id: str | None,
    country: str | None,
    date: str | None,
    end_date: str | None,
    get_calendar_events: Optional[bool] = None,
    get_notes: Optional[bool] = None,
    get_tasks: Optional[bool] = None,
    opportunity_id: str | None,
    limit: int | None,
    order: str | None,
    page: int | None,
    pipeline_id: str | None,
    pipeline_stage_id: str | None,
    q: str | None,
    start_after: str | None,
    start_after_id: str | None,
    status: str | None
) -> dict[str, Any]:
    url = f"{API_BASE_URL}/opportunities/search"
    
    if "Authorization" not in headers or not headers["Authorization"].startswith("Bearer "):
        raise ValueError("Missing or invalid Authorization header")
    
    request_headers = {
        "Authorization": headers["Authorization"],
        "Version": headers.get("Version", API_VERSION),
        "Accept": "application/json"
    }
    
    params = {
        "location_id": location_id,
        "assigned_to": assigned_to,
        "campaignId": campaign_id,
        "contact_id": contact_id,
        "country": country,
        "date": date,
        "endDate": end_date,
        "getCalendarEvents": get_calendar_events,
        "getNotes": get_notes,
        "getTasks": get_tasks,
        "id": opportunity_id,
        "limit": limit,
        "order": order,
        "page": page,
        "pipeline_id": pipeline_id,
        "pipeline_stage_id": pipeline_stage_id,
        "q": q,
        "startAfter": start_after,
        "startAfterId": start_after_id,
        "status": status
    }
    
    params = {k: v for k, v in params.items() if v is not None}
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=request_headers, params=params)
        response.raise_for_status()
        return response.json()