from flask import request
from flask_restplus import Resource
from app.main.model.campaign import Campaign
from app.main.util.campaigndto import CampaignDto
from app.main.config import Config
import datetime
import json
from app.main.service.campaign_service import getAllCampaign, get_Campaign_Onuuid,post_campaign

api = CampaignDto.api
_user = CampaignDto.res_sources
_user1 = CampaignDto.send_campaign

#@api.route("api/test")
#class Registration(Resource):
#    def get(self):
#        return {"manfo": "tandn"}

@api.route('api/v1.0/campaign')
class UserList(Resource):
    @api.doc('list_of_campaign')
    @api.marshal_list_with(_user)
    def get(self):
        """List all campaign"""
        return getAllCampaign()
    
    @api.expect(_user1)
    @api.marshal_with(_user)  
    def post(self):
        data = request.json
        print('hii')
        if type(data) is str:  
            data = json.loads(data)
        return post_campaign(data)


@api.route("api/v1.0/campaign/<uuid>")
class CampaignController(Resource):
    @api.marshal_with(_user)
    def get(self, uuid):
        return get_Campaign_Onuuid(uuid)


 





    

    



