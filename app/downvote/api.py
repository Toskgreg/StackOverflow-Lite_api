"""This module handles the class DOWNVOTEApi and its post method"""
import uuid
from flask.views import MethodView
from flask import jsonify
from app.models import *


class DOWNVOTEAPI(MethodView):
    """This class-based view for downvoting a answer."""
    @staticmethod
    def post(question_id, answer_id):
        '''Method for a post request'''
        question_id = uuid.UUID(question_id)
        answer_id = uuid.UUID(answer_id)
        res = Down_vote.down_vote_on_answer(question_id, answer_id)
        return jsonify({'msg': res}), 201
        
