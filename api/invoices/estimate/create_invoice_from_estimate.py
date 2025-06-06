import httpx
from typing import  Any

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def create_invoice_from_estimate(
    headers: dict[str, str],
    estimate_id: str,
    alt_id: str,
    alt_type: str = "location",
    mark_as_invoiced: bool = True,
    version: str = "v1"
) -> dict[str, Any]:
    url = f"{API_BASE_URL}/invoices/estimate/{estimate_id}/invoice"
    
    if not headers.get("Authorization") or not headers["Authorization"].startswith("Bearer "):
        raise ValueError("Missing or invalid Authorization header. Must be in format: 'Bearer {token}'")

    request_headers = {
        "Authorization": headers["Authorization"],
        "Version": headers.get("Version", API_VERSION),
        "Content-Type": "application/json"
    }
    
    data = {
        "altId": alt_id,
        "altType": alt_type,
        "markAsInvoiced": mark_as_invoiced,
        "version": version
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=request_headers, json=data)
        response.raise_for_status()
        return response.json()