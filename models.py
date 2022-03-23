from enum import unique
from ipaddress import ip_address
from flask_login import UserMixin
from __init__ import db

class Users(UserMixin, db.Model):
    ip_address = db.Column(db.String(100), primary_key=True)
    val = db.Column(db.Integer)