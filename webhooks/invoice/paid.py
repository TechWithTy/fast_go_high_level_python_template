from datetime import datetime
from typing  list

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

router = APIRouter()

class BusinessDetails(BaseModel):
    name: str
    address: str
    phoneNo: str
    website: str
    logoUrl: str
    customValues: list[str]

class Address(BaseModel):
    countryCode: str
    addressLine1: str
    addressLine2: str
    city: str
    state: str
    postalCode: str

class AdditionalEmail(BaseModel):
    email: str

class ContactDetails(BaseModel):
    id: str
    phoneNo: str
    email: str
    customFields: list[str]
    name: str
    address: Address
    additionalEmails: list[AdditionalEmail]
    companyName: str

class Discount(BaseModel):
    type: str
    value: float

class InvoiceItem(BaseModel):
    taxes: list[dict]
    _id: str
    productId: str
    priceId: str
    currency: str
    name: str
    qty: int
    amount: float

class TotalSummary(BaseModel):
    subTotal: float
    discount: float

class Invoice(BaseModel):
    _id: str
    status: str
    liveMode: bool
    amountPaid: float
    altId: str
    altType: str
    name: str
    businessDetails: BusinessDetails
    invoiceNumber: str
    currency: str
    contactDetails: ContactDetails
    issueDate: str
    dueDate: str
    discount: Discount
    invoiceItems: list[InvoiceItem]
    total: float
    title: str
    amountDue: float
    createdAt: datetime
    updatedAt: datetime
    totalSummary: TotalSummary

@router.post("/webhooks/invoice/paid", status_code=status.HTTP_200_OK)
def handle_paid_invoice(invoice: Invoice):
    """
    FastAPI endpoint: Called whenever an invoice is paid via webhook.
    Receives invoice data as JSON and processes it.
    """
    # TODO: Add business logic for handling a paid invoice
    # Example: update database, notify users, etc.
    return JSONResponse(content={"message": "Invoice processed", "invoiceId": invoice._id})

# To use this router, include it in your FastAPI app:
# from .webhooks.invoice import paid
# app.include_router(paid.router)