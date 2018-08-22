"""This module handles QUESTIONAPI class and its methods"""
import uuid
from flask.views import MethodView
from flask import jsonify, request, make_response
from app.models import Question,QUESTIONS


class QUESTIONAPI(MethodView):
    """This class based view handles question related methods"""
    @staticmethod
    def get(question_id):
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

    @staticmethod
    def post():
        '''Method for a post request'''
        data = request.json
        question_title = data["question_title"]
        question_description = data["question_description"]
        res = Question.ask_question(question_title, question_description)
        if res == "Your question has been successfully asked.":
            return jsonify({'msg': res}), 201
        return jsonify({'msg': res}), 201
