import requests
, Optional
from datetime import datetime

def create_invoice_schedule(
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
    attachments: list[dict]
) -> dict:
    url = "https://services.leadconnectorhq.com/invoices/schedule"
    
    if "Authorization" not in headers or not headers["Authorization"].startswith("Bearer "):
        raise ValueError("Invalid or missing Authorization header")
    
    headers.setdefault("Version", "2021-07-28")
    
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
        "paymentMethods": payment_methods,
        "attachments": attachments
    }
    
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()