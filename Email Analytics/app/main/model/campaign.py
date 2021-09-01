from app.main import db
from mongoengine import *
import uuid

class content(db.EmbeddedDocument):
    subject = db.StringField(),
    sender = db.StringField(),
    messageBody = db.StringField(),
    date = db.StringField(),
    receiver = db.StringField()

class Campaign(db.Document):

    uuid = db.UUIDField(default=uuid.uuid4, binary=False)
    name = db.StringField(max_length=100, nullable=True)
    brandId = db.StringField(binary=False, null=True)
    brand = db.StringField(max_length=100, nullable=True)
    description = db.StringField(max_length=100, nullable=True)
    #created_at = db.LongField(nullable=True)
    #updated_at = db.LongField(nullable=True)
    createdAt = db.StringField()
    updatedAt = db.StringField()
    keywords = db.ListField(db.StringField(max_length=20))
    #subject = db.StringField()
    #sender = db.StringField()
    #messageBody = db.StringField()
    #date = db.StringField()
    #receiver = db.StringField()
    contentdetails = db.EmbeddedDocumentField(content)
    

