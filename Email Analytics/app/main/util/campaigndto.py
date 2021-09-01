#from app.main.service.campaign_service import post_campaign
from flask_restplus import Namespace, fields

class CampaignDto:
    api = Namespace('user', description='campaign related operations')
    CONTENTDETAILS = api.model(
        'CONTENTDETAILS', 
        {
         'subject': fields.String(required=True, description='subject'),
         'sender': fields.String(required=True, description='sender'),
         'messageBody': fields.String(required=True, description='messagebody'),
         'date': fields.String(required=True, description='date'),
         'receiver':fields.String(required=True, description="receiver"),
        },
    )

    res_campaign = api.model('res_campaign', {
        'uuid':fields.String(required=True, decription='campaign id'),
        'name': fields.String(required=True, description='name'),
        'brandId': fields.String(required=True, description='brandid'),
        'brand': fields.String(required=True, description='brand'),
        'description': fields.String(required=True, description='description'),
        'createdAt': fields.String(required=True, description='data inserted at'),
        'updatedAt': fields.String(required=True, description='last update'),
        'keywords': fields.List(fields.String (required=True, description='keywords')),
        'contentdetails':fields.Nested(CONTENTDETAILS)  
    })

    res_sources = api.model('response of all sources', {
        'data': fields.List(fields.Nested(res_campaign),attribute="data",)
    })


    send_campaign = api.model('send_campaign',{
        'name': fields.String(required=True, description='name'),
        'brandId': fields.String(required=True, description='brandid'),
        'brand': fields.String(required=True, description='brand'),
        'description': fields.String(required=True, description='description'),
        'keywords': fields.List(fields.String (required=True, description='keywords')),
        'contentdetails':fields.Nested(CONTENTDETAILS)  
        #'subject': fields.String(required=True, description='subject'),
        #'sender': fields.String(required=True, description='sender'),
        #'messageBody': fields.String(required=True, description='messagebody'),
        #'receiver':fields.String(required=True, description="receiver") 
    })

   

    
  