import httpx
from typing import  Any

async def manage_auto_payment(schedule_id: str, alt_id: str, alt_type: str, auto_payment: dict[str, Any], headers: dict[str, str]) -> dict[str, Any]:
    url = f"https://services.leadconnectorhq.com/invoices/schedule/{schedule_id}/auto-payment"
    
    if not headers.get("Authorization") or not headers["Authorization"].startswith("Bearer "):
        raise ValueError("Missing or invalid Authorization header. Must be in format: 'Bearer {token}'")

    request_headers = {
        "Authorization": headers["Authorization"],
        "Version": headers.get("Version", "2021-07-28"),
        "Content-Type": "application/json"
    }
    
    payload = {
        "altId": alt_id,
        "altType": alt_type,
        "id": schedule_id,
        "autoPayment": auto_payment
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=request_headers, json=payload)
        response.raise_for_status()
    
    return response.json()