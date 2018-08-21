"""This module contains classes Question,Answer,Upvote,Downvote,comments and their methods"""
import uuid
from datetime import datetime as dt
from flask import jsonify, request, abort, make_response
QUESTIONS = []
ANSWERS = []
COMMENTS = []



class Question(object):
    ''' A Questions class'''

    def __init__(
            self,
            question_id,
            question_title,
            date_created,
            date_modified,
            question_description,
            answers):
        ''' Initializes the question object'''
        self.question_id = question_id
        self.question_title = question_title
        self.date_created = dt.utcnow()
        self.date_modified = dt.utcnow()
        self.question_description = question_description
        self.answers = ANSWERS

    @classmethod
    def question_already_exists(cls, question_title, question_description):
        """A method to check if the same question already exists """
        for question in QUESTIONS:
            if question['question_title'] == question_title and question['question_description'] == \
                    question_description:
                return True
        return False

    @classmethod
    def view_all_questions(cls):
        """ Return all the questions asked on the forum."""
        return QUESTIONS

    @classmethod
    def view_question_by_ID(cls,question_id):
        for question in QUESTIONS:
            if question_id == question['Id']:
                return question
        
    @classmethod
    def ask_question(cls, question_title, question_description):
        """A method for asking a question"""
        cls.data = {}
        if cls.question_already_exists(question_title, question_description):
            return "question already exists"
        else:
            cls.data['Id'] = uuid.uuid1()
            cls.data['date_created'] = dt.utcnow()
            cls.data['date_modified'] = dt.utcnow()
            cls.data['question_title'] = question_title
            cls.data['question_description'] = question_description
            cls.data['answers'] = ANSWERS

            QUESTIONS.append(cls.data)
            return "Your question has been successfully asked."

class Answer(object):
    def __init__(
            self,
            text,
            answer_id,
            question_id,
            accepted,
            up_vote,
            downvote,
            date_answered,
            comments):
        self.text = text
        self.answer_id = answer_id
        self.up_vote = 0
        self.down_vote = 0
        self.comments = COMMENTS
        self.accepted = False
        self.date_answered = dt.utcnow()

    @classmethod
    def answer_question(cls, question_id, text):
        """A method for posting a answer"""
        for question in QUESTIONS:
            if question['Id'] == question_id:
                cls.data1 = {}
                cls.data1['Id'] = uuid.uuid1()
                cls.data1['text'] = text
                cls.data1['up_vote'] = 0
                cls.data1['down_vote'] = 0
                cls.data1['comment'] = COMMENTS
                cls.data1['accepted'] = False
                cls.data1['date_answered'] = dt.utcnow()

                ANSWERS.append(cls.data1)
                return "You have successfully answered the question."