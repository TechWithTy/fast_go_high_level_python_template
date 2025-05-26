import httpx
from typing  list, Optional
from datetime import datetime

async def create_invoice_schedule(
    headers: dict[str, str],
    alt_id: str,
    alt_type: str,
    name: str,
    contact_details: dict,
    schedule: dict,
    live_mode: bool,
    business_details: dict,
    currency: str,
    items: list[dict],
    automatic_taxes_enabled: bool,
    discount: dict,
    terms_notes: str,
    title: str,
    tips_configuration: dict,
    late_fees_configuration: dict,
    invoice_number_prefix: str,
    payment_methods: dict,
    attachments: list[dict] | None = None
) -> dict:
    url = "https://services.leadconnectorhq.com/invoices/schedule"
    
    if not headers.get("Authorization") or not headers["Authorization"].startswith("Bearer "):
        raise ValueError("Missing or invalid Authorization header. Must be in format: 'Bearer {token}'")
    
    if not headers.get("Version"):
        raise ValueError("Missing Version header")
    
    payload = {
        "altId": alt_id,
        "altType": alt_type,
        "name": name,
        "contactDetails": contact_details,
        "schedule": schedule,
        "liveMode": live_mode,
        "businessDetails": business_details,
        "currency": currency,
        "items": items,
        "automaticTaxesEnabled": automatic_taxes_enabled,
        "discount": discount,
        "termsNotes": terms_notes,
        "title": title,
        "tipsConfiguration": tips_configuration,
        "lateFeesConfiguration": late_fees_configuration,
        "invoiceNumberPrefix": invoice_number_prefix,
        "paymentMethods": payment_methods
    }
    
    if attachments:
        payload["attachments"] = attachments
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)
        response.raise_for_status()
    
    return response.json()