"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field
from typing import Optional, Literal

# Example schemas (you may keep these for reference)

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)

    Used for: Verkoop & Onderdelen
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Short description / state")
    category: Literal['Auto', 'Landbouw', 'Diversen'] = Field('Diversen', description="Product category")
    price: Optional[float] = Field(None, ge=0, description="Optional fixed price; if None, price on request")
    condition: Optional[str] = Field(None, description="State/Condition e.g. Nieuw, Gebruikt, Dealer onderhouden")
    image_url: Optional[str] = Field(None, description="Public image URL for the product card")

class Appointment(BaseModel):
    """
    Appointment requests
    Collection name: "appointment"

    Used for: Contact & Afspraak formulier
    """
    name: str = Field(..., min_length=2, description="Naam klant")
    phone: str = Field(..., min_length=6, description="Telefoonnummer")
    email: Optional[str] = Field(None, description="E-mailadres")
    service_type: Literal['APK', 'Auto onderhoud', 'Diagnose', 'Tractorreparatie', 'Hydrauliek', 'Onderhoud op locatie', 'Overig'] = 'Overig'
    preferred_date: Optional[str] = Field(None, description="Voorkeursdatum (tekst)")
    message: Optional[str] = Field(None, description="Korte toelichting of kenteken")

# Add your own schemas here if needed.
