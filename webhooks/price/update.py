
from pydantic import BaseModel, Field
from datetime import datetime

class MembershipOffer(BaseModel):
    label: str
    value: str
    _id: str

class Recurring(BaseModel):
    interval: str
    intervalCount: int

class PriceUpdate(BaseModel):
    _id: str
    membershipOffers: list[MembershipOffer]
    variantOptionIds: list[str]
    locationId: str
    product: str
    userId: str
    name: str
    type: str
    currency: str
    amount: float
    recurring: Recurring
    createdAt: datetime
    updatedAt: datetime
    compareAtPrice: float
    trackInventory: Optional[bool] = None
    availableQuantity: int
    allowOutOfStockPurchases: bool
