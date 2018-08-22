"""This module handles the class UPVOTEApi and its post method"""
import uuid
from flask.views import MethodView
from flask import jsonify
from app.models import *


class Up(MethodView):
    """This class-based view for UPVOTING a ANSWER."""
    @staticmethod
    def post(question_id, answer_id):
        '''Method for a post request'''
        question_id = uuid.UUID(question_id)
        answer_id = uuid.UUID(answer_id)
        res = Up_vote.up_vote_on_answer(question_id, answer_id)
        return jsonify({'msg': res}), 201
        
