from app.main import db
from app.main.model.campaign import Campaign
from werkzeug.exceptions import BadRequest
from http import HTTPStatus
import calendar
import time

def post_campaign(data):
    name = data['name']
    dat = Campaign.objects(name=name).first()
    if dat:
        raise BadRequest("campaign name already exists")
#    try:
    print(data['contentdetails'])
    save_con = Campaign(
        #uuid=data['uuid'],
        name=data['name'],
        brandId=data['brandId'],
        brand=data['brand'],
        description=data['description'],
        #created_at=data['created_at'],
        #updated_at=data['updated_at'],
        createdAt=str(calendar.timegm(time.gmtime())),
        updatedAt=str(calendar.timegm(time.gmtime())),
        keywords=data['keywords'],
        contentdetails = data['contentdetails'],
        #subject=data['subject'],
        #sender=data['sender'],
        #messageBody=data['messageBody'],
        #date=str(calendar.timegm(time.gmtime())),
        #receiver=data['receiver']
    )
    save_con.save()
    return save_con, HTTPStatus.CREATED.value
#    except:
#        raise BadRequest(f"Not able to save Campaign")


def getAllCampaign():
    try:
        data = Campaign.objects()
        print(data)
        return {"data": data}, HTTPStatus.OK.value
    except:
        raise BadRequest(f"Registered campaign not found")


def get_Campaign_Onuuid(uuid):
    camp = Campaign.objects(uuid=uuid).first()
    print(camp)
    if not camp:
        raise BadRequest(f"campaign not found please check uuid")
    return {"data": camp}, HTTPStatus.OK.value


