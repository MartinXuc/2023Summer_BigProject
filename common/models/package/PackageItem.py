from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from ..db import db




class PackageItem(db.Model):
    __tablename__ = 'package_item'

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    package_id = db.Column(db.Integer, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    effective_date = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    valid_period = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
