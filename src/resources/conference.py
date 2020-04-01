"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import UserRepository
from util import parse_params


# POST 
# 200 response
# 409 response - if conference room exists - message - room not availble at the moment
class Conference(Resource):
    """ Verbs relative to the conference """

    @staticmethod
    @parse_params(
        Argument("name", location="query", required=True, help="short name of the conference room(not full MUC address)."),
        Argument("start_time", location="query", required=True, help="conference start date and time."),
        Argument("mail_owner", location="query", required=True, help="if authentication system is enabled this field will contain user's identity. It that case it will not be possible to create new conference room without authenticating.")
    )
    @swag_from("../swagger/conference/POST.yml")
    def post(name, start_time, mail_owner):
        """ Create an user based on the sent information """
        # user = UserRepository.create(
        #     last_name=last_name, first_name=first_name, age=age
        # )
        # return jsonify({"user": user.json})
        return jsonify({"get": name})


# /{id}
# GET
# DELETE
class ConferenceItem(Resource):
    """ Verbs relative to the conference with {conference_id} """

    @staticmethod
    @parse_params(
        Argument("conference_id", location="path", required=True, help="Conference ID")
    )
    @swag_from("../swagger/conference/GET.yml")
    def get(conference_id):
        """ Get conference info based on conference id """
        # user = UserRepository.create(
        #     last_name=last_name, first_name=first_name, age=age
        # )
        # return jsonify({"user": user.json})
        return jsonify({"get": conference_id})

    @staticmethod
    @parse_params(
        Argument("conference_id", location="path", required=True, help="Conference ID")
    )
    @swag_from("../swagger/conference/DELETE.yml")
    def delete(conference_id):
        """ Delete conference info based on conference id """
        # user = UserRepository.create(
        #     last_name=last_name, first_name=first_name, age=age
        # )
        # return jsonify({"user": user.json})
        return jsonify({"delete": conference_id})