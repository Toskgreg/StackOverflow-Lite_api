"""This module contains classes Question,Answer,Upvote,Downvote,comments and their methods"""
import uuid
from datetime import datetime as dt
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
    def question_fields_empty(cls, question_title, question_description):
        """A method to check if the user is trying to enter empty fields """
        if question_title.strip() == '' or question_description.strip() == '':
            return True
        

    @classmethod
    def view_all_questions(cls):
        """ Return all the questions asked on the forum."""
        return QUESTIONS

    @classmethod
    def view_question_by_ID(cls, question_id):
        for question in QUESTIONS:
            if question_id == question['Id']:
                return question
            return "Your question has been successfully asked."

    @classmethod
    def ask_question(cls, question_title, question_description):
        """A method for asking a question"""
        cls.data = {}
        if cls.question_fields_empty(question_title, question_description):
            return "Dear user you can not enter empty fields. Please fill them"
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

    def answer_fields_empty(cls, text):
        """A method to check if the user is trying to enter empty answer field """
        if text.strip() == '':
            return True

    @classmethod
    def answer_question(cls, question_id, text):
        """A method for posting a answer"""
        if cls.answer_fields_empty(question_id,text):
            return "Dear user you can not enter empty fields. Please fill them"
        else:
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


class Comment(object):
    def __init__(self, text1, answer_id, question_id, date_commented):
        self.text1 = text1
        self.answer_id = answer_id
        self.question_id = question_id
        self.date_commented = dt.utcnow()

    @classmethod
    def comment_on_answer(cls, question_id, answer_id, text1):
        """A method for posting a comment to a answer"""
        for question in QUESTIONS:
            if question['Id'] == question_id:
                for answer in ANSWERS:
                    if answer['Id'] == answer_id:
                        cls.data2 = {}
                        cls.data2['Id'] = uuid.uuid1()
                        cls.data2['text1'] = text1
                        cls.data2['date_commented'] = dt.utcnow()

                        COMMENTS.append(cls.data2)
                        return "You have successfully commented on the answer."


class Up_vote(object):
    def __init__(self, answer_id, question_id):
        self.answer_id = answer_id
        self.question_id = question_id

    @classmethod
    def up_vote_on_answer(cls, question_id, answer_id):
        """A method for upvoting a answer"""
        for question in QUESTIONS:
            if question['Id'] == question_id:
                for answer in ANSWERS:
                    if answer['Id'] == answer_id:
                        answer['up_vote'] = answer['up_vote'] + 1
                        return "You have successfully upvoted the answer."


class Down_vote(object):
    def __init__(self, answer_id, question_id):
        self.answer_id = answer_id
        self.question_id = question_id

    @classmethod
    def down_vote_on_answer(cls, question_id, answer_id):
        """A method for downvoting a answer"""
        for question in QUESTIONS:
            if question['Id'] == question_id:
                for answer in ANSWERS:
                    if answer['Id'] == answer_id:
                        answer['down_vote'] = answer['down_vote'] + 1
                        return "You have successfully downvoted the answer."
