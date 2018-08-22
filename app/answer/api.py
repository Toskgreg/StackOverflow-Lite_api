import uuid
from flask.views import MethodView
from flask import jsonify, request
from app.models import ANSWERS,QUESTIONS,Question,Answer


class AnswerAPI(MethodView):
    """This class-based view for answering a question."""
    @staticmethod
    def post(question_id):
        '''Method for a post answer'''
        question_id = uuid.UUID(question_id)
        data = request.json
        text = data["text"]
        res = Answer.answer_question(question_id, text)
        if res == "You have successfully answered the question.":
            return jsonify({'msg': res}), 201
        return jsonify({'msg': res}), 409
