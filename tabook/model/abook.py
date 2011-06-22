# -*- coding: utf-8 -*-
"""
Address book related model.
"""
import os
from datetime import datetime
import sys
try:
    from hashlib import sha1
except ImportError:
    sys.exit("ImportError: No module named hashlib\n"
             "If you are on python2.4 this library is not part of python. "
             "Please install it. Example: easy_install hashlib")

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, DateTime
from sqlalchemy.orm import relation, synonym

from tabook.model import DeclarativeBase, metadata, DBSession

__all__ = ["Card", "Address"]


class Card(DeclarativeBase):
    __tablename__ = "card"

    id = Column(Integer, autoincrement=True, primary_key=True)
    first_name = Column(Unicode(255), unique=True, nullable=False)
    last_name = Column(Unicode(255), unique=True, nullable=False)
    addresses = relation("Address", backref="cards")

    #{ Special methods

    def __repr__(self):
        return ("<Card: name=%s %s>" % (self.first_name, self.last_name)).encode("utf-8")

    def __unicode__(self):
        return ("%s %s" % (self.first_name, self.last_name)).encode("utf-8")


class Address(DeclarativeBase):
    __tablename__ = "address"

    id = Column(Integer, autoincrement=True, primary_key=True)
    address = Column(Unicode(255), nullable=False)
    zip_code = Column(Unicode(16), nullable=False)
    phone_number = Column(Unicode(16), nullable=False)
    lat_long = Column(Unicode(255), nullable=False)
    card_id = Column(Integer, ForeignKey('card.id'))

    def __repr__(self):
        return ("<Address: %s>" % self.address).encode("utf-8")

    def __unicode__(self):
        return self.address
