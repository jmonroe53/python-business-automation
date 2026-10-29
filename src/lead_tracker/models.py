"""Lead data model. Practice dictionaries or dataclasses here."""

from dataclasses import dataclass


@dataclass
class Lead:
    name: str
    email: str
    source: str
    interest: int  # Suggested range: 1–5
