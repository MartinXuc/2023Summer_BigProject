from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from ..db import db

from application import app


class Package(db.Model):
    __tablename__ = 'package'

    id = db.Column(db.Integer, primary_key=True)
    discount = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    food_id = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    type = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
