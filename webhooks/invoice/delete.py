from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

router = APIRouter()


class InvoiceDeletePayload(BaseModel):
    _id: str
    status: str | None
    invoiceNumber: str | None
    amountDue: str | None


@router.post("/webhooks/invoice/delete", status_code=status.HTTP_200_OK)
def invoice_deleted_webhook(payload: InvoiceDeletePayload):
    """
    FastAPI endpoint: Called whenever an invoice is deleted via webhook.
    Receives invoice data as JSON and processes it.
    """
    # Extract relevant information from the payload
    invoice_id = payload._id
    status_ = payload.status
    invoice_number = payload.invoiceNumber
    amount_due = payload.amountDue

    # Process the deleted invoice
    # Add your business logic here, e.g., updating database, sending notifications, etc.

    # Example: Print some information about the deleted invoice
    print(f"Invoice {invoice_number} (ID: {invoice_id}) has been deleted.")
    print(f"Status: {status_}")
    print(f"Amount due: {amount_due}")

    return JSONResponse(
        content={"message": "Invoice deleted processed", "invoiceId": invoice_id}
    )


# To use this router, include it in your FastAPI app:
# from .webhooks.invoice import delete
# app.include_router(delete.router)
