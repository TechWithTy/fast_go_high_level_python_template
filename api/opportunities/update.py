from typing import  Any, Optional
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def update_opportunity(
    headers: dict[str, str],
    opportunity_id: str,
    pipeline_id: str | None,
    name: str | None,
    pipeline_stage_id: str | None,
    status: str | None,
    monetary_value: float | None = None,
    assigned_to: str | None,
    custom_fields: Optional[list[dict[str, str]]] = None
) -> dict[str, Any]:
    url = f"{API_BASE_URL}/opportunities/{opportunity_id}"
    
    if not headers.get("Authorization") or not headers["Authorization"].startswith("Bearer "):
        raise ValueError("Missing or invalid Authorization header. Must be in format: 'Bearer {token}'")
    
    request_headers = {
        "Authorization": headers["Authorization"],
        "Version": headers.get("Version", API_VERSION),
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    payload = {}
    if pipeline_id:
        payload["pipelineId"] = pipeline_id
    if name:
        payload["name"] = name
    if pipeline_stage_id:
        payload["pipelineStageId"] = pipeline_stage_id
    if status:
        payload["status"] = status
    if monetary_value is not None:
        payload["monetaryValue"] = monetary_value
    if assigned_to:
        payload["assignedTo"] = assigned_to
    if custom_fields:
        payload["customFields"] = custom_fields
    
    async with httpx.AsyncClient() as client:
        response = await client.put(url, headers=request_headers, json=payload)
    
    response.raise_for_status()
    return response.json()