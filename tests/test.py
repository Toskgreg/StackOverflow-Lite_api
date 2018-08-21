from run import app
import unittest
import uuid
from flask import json
from app.answer import views
from app.question import views


class TestAnswer(unittest.TestCase):
    def setUp(self):
        """This instanciates the flask app for a background no-live-server operations for testing purposes"""
        self.app = app.test_client()

    def test_question_creation(self):
        """Test API can create a question (POST request)"""
        response = self.app.post('api/v1/questions/',
                                 content_type='application/json',
                                 data=json.dumps({
                                     "question_title": "What is an API ?",
                                     "question_description": " in detail what an API is?"
                                 }))

        self.assertEqual(response.status_code, 201)
        self.assertIn(
            'Your question has been successfully asked.', str(
                response.data))

    def test_return_created_code_if_answer_is_valid(self):
        """This method checks if a valid answer has been posted and returns an apropriate status code 201"""
        # post data
        response = self.app.post('api/v1/questions/',
                                 content_type='application/json',
                                 data=json.dumps({
                                     "question_title": "What is an API ?",
                                     "question_description": " in detail what an API is?"
                                 }))

        self.assertEqual(response.status_code, 201)
        self.assertIn(
            'Your question has been successfully asked.', str(
                response.data))
        response = self.app.get('api/v1/questions/')
        self.assertEqual(response.status_code, 200)

        results = json.loads(response.data.decode())

        for question in results:
            response = self.app.post('api/v1/questions/{}/answer/'
                                     .format(question['Id']),
                                     content_type='application/json',
                                     data=json.dumps({
                                         "text": "This is a simple answer",
                                     }))
            self.assertEqual(response.status_code, 201)
            self.assertIn(
                "You have successfully answered the question.",
                str(response.data))

    def test_api_can_view_all_questions(self):
        """Test QUESTIONAPI can view all (GET request)."""
        response = self.app.post('api/v1/questions/',
                                 content_type='application/json',
                                 data=json.dumps({
                                     "question_title": "What is an API ?",
                                     "question_description": " in detail what an API is?"
                                 }))

        self.assertEqual(response.status_code, 201)
        response = self.app.get('api/v1/questions/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("title", str(response.data))

    def test_api_can_get_question_by_id(self):
        """Test API can fetch a single question by using it's id."""
        # post data
        response = self.app.post('api/v1/questions/',
                                 content_type='application/json',
                                 data=json.dumps({
                                     "question_title": "What is an API ?",
                                     "question_description": " in detail what an API is?"
                                 }))
        self.assertEqual(response.status_code, 201)
        response = self.app.get('api/v1/questions/')
        self.assertEqual(response.status_code, 200)

        results = json.loads(response.data.decode())
        for question in results:
            result = self.app.get(
                'api/v1/questions/{}'.format(question['Id']))
            self.assertEqual(result.status_code, 200)
            self.assertIn(question['Id'], str(result.data))
