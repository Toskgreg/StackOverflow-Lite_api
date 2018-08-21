[![Coverage Status](https://coveralls.io/repos/github/Toskgreg/StackOverflow-Lite_api/badge.svg?branch=develop)](https://coveralls.io/github/Toskgreg/StackOverflow-Lite_api?branch=develop)
[![Build Status](https://travis-ci.org/Toskgreg/StackOverflow-Lite_api.svg?branch=develop)](https://travis-ci.org/Toskgreg/StackOverflow-Lite_api)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d9559d4690e544f7ac013e875e77e0f1)](https://www.codacy.com/project/Toskgreg/StackOverflow-Lite_api/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Toskgreg/StackOverflow-Lite_api&amp;utm_campaign=Badge_Grade_Dashboard)
# StackOverflow-lite
StackOverflow-lite is a question and answer application that provides users with the ability to ask questions and have other users answer the questions

## DESCRIPTION

Stackoverflow-lite is a platform where people can ask questions and provide answers

## Link to Stackoverflow-lite on Github Pages

[Stackoverflow-lite](https://toskgreg.github.io/StackOverflow-lite/)

## Link to Stackoverflow-lite API hosted on heroku

[StackOverflow-Lite_api](https://git.heroku.com/stackoverflow-lite12.git)

### Tools

* Text editor where we write our project files. (VScode)
* Python
* Flask Python Framework -Server-side framework
* Pytest - a Python Testing Framework
* Pylint - a Python linting library 
* Postman -Application to test and consume endpoints
* PEP8 - Style guide

## Routes captured by Stackoverflow-lite

 REQUEST | ROUTE | FUNCTIONALITY
 ------- | ----- | -------------
 GET | /api/v1/questions | Fetches all questions
 POST | /api/v1/questions | Posts a question
 GET | /api/v1/question/< questionId> | Fetches a specific question
 POST | /api/v1/questions/< question_Id>/answer/ | Post an answer to a question
 POST | /api/v1/questions/< question_Id>/< answer_id>/comment | Post a comment to answer
 POST | /api/v1/questions/< question_Id>/< answer_id>/upvote | Upvote answer
 POST | /api/v1/questions/< question_Id>/< answer_id>/downvote | Downvote  answer


## BUIT WITH

 * Flask-Python

## HOW TO RUN THE APPLICATION

 ### SETING UP THE ENVIRONMENT
 
 1. Clone this repository to your local PC

    ` git clone https://github.com/Toskgreg/StackOverflow-Lite_api.git `

 2. Create a virtual environment to run application specific dependencies

    ` $ virtualenv venv `
    ` $ source venv/bin/activate `
    ` $ pip install flask `

 ### RUN THE APP

 1. To run the app

    ` python run.py `

 2. To run tests
    `  python -m pytest --cov tests/ `
## Author

**Toskin Gregory**
