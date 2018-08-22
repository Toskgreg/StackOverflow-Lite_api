"""This module handles the class COMMENTApi and its post method"""
import uuid
from flask.views import MethodView
from flask import jsonify, request
from app.models import Comment


class COMMENTAPI(MethodView):
    """This class-based view for COMMENTING on a question."""
    @staticmethod
    def post(question_id, answer_id):
        '''Method for a post request'''
        question_id = uuid.UUID(question_id)
        answer_id = uuid.UUID(answer_id)
        data = request.json
        text1 = data["text1"]
        res = Comment.comment_on_answer(question_id, answer_id, text1)
        return jsonify({'msg': res}), 201
