"""
Address book related model
"""
from sqlalchemy import ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, Float
from sqlalchemy.orm import relation

from tabook.model import DeclarativeBase

__all__ = ["Card", "Address"]


class Card(DeclarativeBase):
    """
    Person card
    """
    __tablename__ = "card"

    id = Column(Integer, autoincrement=True, primary_key=True)
    first_name = Column(Unicode(255), nullable=False)
    last_name = Column(Unicode(255), nullable=False)
    email = Column(Unicode(255), nullable=False)
    addresses = relation("Address", backref='user',
                         cascade="all, delete, delete-orphan")

    @property
    def name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __repr__(self):
        return (
            "<Card: name=%s %s>" % (self.first_name, self.last_name)
        ).encode("utf-8")

    def __unicode__(self):
        return ("%s %s" % (self.first_name, self.last_name)).encode("utf-8")


class Address(DeclarativeBase):
    """
    Address attached to card
    """
    __tablename__ = "address"

    id = Column(Integer, autoincrement=True, primary_key=True)
    address = Column(Unicode(255), nullable=False)
    zip_code = Column(Unicode(5), nullable=False)
    state = Column(Unicode(2), nullable=False)
    phone_number = Column(Unicode(16), nullable=False)
    lat = Column(Float)
    lng = Column(Float)
    card_id = Column(Integer, ForeignKey("card.id"), nullable=False)

    def __repr__(self):
        return ("<Address: %s>" % self.address).encode("utf-8")

    def __unicode__(self):
        return self.address
