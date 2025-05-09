import httpx
from typing , list, Any, Optional

async def create_invoice(
    headers: dict[str, str],
    alt_id: str,
    name: str,
    contact_id: str,
    contact_name: str,
    issue_date: str,
    items: list[dict[str, Any]],
    currency: str = "USD",
    alt_type: str = "location",
    business_details: dict[str, Any] = None,
    discount: dict[str, Any] = None,
    terms_notes: str | None,
    title: str = "INVOICE",
    contact_details: dict[str, Any] = None,
    invoice_number: str | None,
    due_date: str | None,
    sent_to: Optional[dict[str, list[str]]] = None,
    live_mode: bool = True,
    automatic_taxes_enabled: bool = False,
    payment_schedule: dict[str, Any] = None,
    late_fees_config: dict[str, Any] = None,
    tips_config: dict[str, Any] = None,
    invoice_number_prefix: str | None,
    payment_methods: dict[str, Any] = None,
    attachments: Optional[list[dict[str, Any]]] = None
) -> dict[str, Any]:
    """
    Create an invoice using GoHighLevel API
    
    Args:
        headers: Dictionary containing Authorization and Version headers
        alt_id: Location ID or company ID
        name: Invoice name
        contact_id: Contact ID
        contact_name: Contact name
        issue_date: Issue date in YYYY-MM-DD format
        items: list of invoice items
        currency: Currency code (default: USD)
        alt_type: Alt type (default: location)
        business_details: Business details
        discount: Discount information
        terms_notes: Terms and notes
        title: Invoice title
        contact_details: Additional contact details
        invoice_number: Invoice number
        due_date: Due date in YYYY-MM-DD format
        sent_to: Email and phone recipients
        live_mode: Live mode flag
        automatic_taxes_enabled: Enable automatic taxes
        payment_schedule: Payment schedule details
        late_fees_config: Late fees configuration
        tips_config: Tips configuration
        invoice_number_prefix: Prefix for invoice number
        payment_methods: Payment methods configuration
        attachments: list of attachments
    
    Returns:
        API response as dictionary
    """
    url = "https://services.leadconnectorhq.com/invoices/"
    
    if not headers.get("Authorization") or not headers["Authorization"].startswith("Bearer "):
        raise ValueError("Missing or invalid Authorization header. Must be in format: 'Bearer {token}'")

    if not headers.get("Version"):
        headers["Version"] = "2021-07-28"

    request_headers = {
        "Authorization": headers["Authorization"],
        "Version": headers["Version"],
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    if contact_details is None:
        contact_details = {"id": contact_id, "name": contact_name}
    
    payload = {
        "altId": alt_id,
        "altType": alt_type,
        "name": name,
        "currency": currency,
        "items": items,
        "contactDetails": contact_details,
        "issueDate": issue_date,
        "title": title,
        "liveMode": live_mode
    }
    
    optional_fields = {
        "businessDetails": business_details,
        "discount": discount,
        "termsNotes": terms_notes,
        "invoiceNumber": invoice_number,
        "dueDate": due_date,
        "sentTo": sent_to,
        "automaticTaxesEnabled": automatic_taxes_enabled,
        "paymentSchedule": payment_schedule,
        "lateFeesConfiguration": late_fees_config,
        "tipsConfiguration": tips_config,
        "invoiceNumberPrefix": invoice_number_prefix,
        "paymentMethods": payment_methods,
        "attachments": attachments
    }
    
    payload.update({k: v for k, v in optional_fields.items() if v is not None})
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=request_headers, json=payload)
        response.raise_for_status()
        return response.json()