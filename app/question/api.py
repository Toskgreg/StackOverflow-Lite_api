"""This module handles QUESTIONAPI class and its methods"""
import uuid
from flask.views import MethodView
from flask import jsonify, request, abort, make_response
from app.models import *


class QUESTIONAPI(MethodView):
    """This class based view handles question related methods"""

    def get(self, question_id):
        """Method for  get requests"""
        if question_id:
            question_id = uuid.UUID(question_id)
            question = Question.view_question_by_ID(question_id)
            return jsonify(question), 200
        else:
            questions = Question.view_all_questions()
            if QUESTIONS == []:
                response = {
                    "msg": " There are no questions at the moment"}
                return make_response(jsonify(response)), 200
            return jsonify(questions), 200
