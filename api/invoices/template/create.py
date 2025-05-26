import aiohttp
import json
from typing import  Any, Optional

async def create_invoice_template(
    headers: dict[str, str],
    alt_id: str,
    alt_type: str = "location",
    internal: bool = True,
    name: str = "New Template",
    business_details: dict[str, Any] = None,
    currency: str = "USD",
    items: Optional[list[dict[str, Any]]] = None,
    automatic_taxes_enabled: bool = True,
    discount: dict[str, Any] = None,
    terms_notes: str | None,
    title: str | None,
    tips_configuration: dict[str, Any] = None,
    late_fees_configuration: dict[str, Any] = None,
    invoice_number_prefix: str | None,
    payment_methods: dict[str, Any] = None,
    attachments: list[str] | None = None
) -> dict[str, Any]:
    url = "https://services.leadconnectorhq.com/invoices/template"
    
    payload = {
        "altId": alt_id,
        "altType": alt_type,
        "internal": internal,
        "name": name,
        "businessDetails": business_details or {},
        "currency": currency,
        "items": items or [],
        "automaticTaxesEnabled": automatic_taxes_enabled,
        "discount": discount or {},
        "termsNotes": terms_notes,
        "title": title,
        "tipsConfiguration": tips_configuration or {},
        "lateFeesConfiguration": late_fees_configuration or {},
        "invoiceNumberPrefix": invoice_number_prefix,
        "paymentMethods": payment_methods or {},
        "attachments": attachments or []
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as response:
            if response.status == 200:
                return await response.json()
            else:
                response.raise_for_status()