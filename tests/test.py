from run import app
import unittest
from flask import json


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

    def test__fields_are_empty(self):
        """Test if a question can be created without data"""
        response = self.app.post('api/v1/questions/',
                                    content_type='application/json',
                                    data=json.dumps({
                                        "question_title":"",
                                        "question_description":""
                                    }))

        self.assertIn("Dear user you can not enter empty fields. Please fill them",
                      str(response.data))

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
            response = self.app.get(
                'api/v1/questions/{}'.format(question['Id']))
            self.assertEqual(response.status_code, 200)

            results1 = json.loads(response.data.decode())
            results2 = json.loads(response.data.decode())
            results3 = json.loads(response.data.decode())

            # The code below tests whether a user can successfully comment on
            # an answer.
            for answer in results1:
                response1 = self.app.post(
                    'api/v1/questions/82b0cdec-a5ff-11e8-87c8-0017a4cf67cb/a56d62c8-a5ff-11e8-8b77-0017a4cf67cb/comment',
                    content_type='application/json',
                    data=json.dumps(
                        {
                            "text1": "hehehehe stop giving wrong answers"}))
            self.assertEqual(response1.status_code, 201)

            # The code below tests whether a user can successfully upvote the
            # answer.
            for answer in results2:
                response = self.app.post(
                    'api/v1/questions/82b0cdec-a5ff-11e8-87c8-0017a4cf67cb/a56d62c8-a5ff-11e8-8b77-0017a4cf67cb/upvote',
                    content_type='application/json')
            self.assertEqual(response.status_code, 201)
            # The code below tests whether a user can successfully downvote the
            # answer.
            for answer in results3:
                response = self.app.post(
                    'api/v1/questions/9f864454-a5fa-11e8-8f2e-0017a4cf67cb/d6d2921c-a5fe-11e8-a075-0017a4cf67cb/downvote',
                    content_type='application/json',
                    data=json.dumps(
                        {}))
            self.assertEqual(response.status_code, 201)

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
