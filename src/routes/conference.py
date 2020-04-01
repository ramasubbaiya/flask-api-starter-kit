"""
Defines the blueprint for the conference
"""
from flask import Blueprint
from flask_restful import Api

from resources import Conference, ConferenceItem

CONFERENCE_BLUEPRINT = Blueprint("conference", __name__)
Api(CONFERENCE_BLUEPRINT).add_resource(
    Conference, "/conference"
)

Api(CONFERENCE_BLUEPRINT).add_resource(
    ConferenceItem, "/conference/<string:conference_id>"
)
