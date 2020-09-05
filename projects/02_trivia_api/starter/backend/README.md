# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
createDb trivia
export FLASK_APP=flaskr
export FLASK_ENV=development
flask db upgrade
using the trivia.sql file in my package not th original run:
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'0' : "Science",
'1' : "Art",
'2' : "Geography",
'3' : "History",
'4' : "Entertainment",
'5' : "Sports"}

```

GET '/questions'
-fetches  a dictionary of questions from all categories, categories ,total number of questions
-request argument: page number, ?page="num"
-returns" an object with 3 keys : 1)questions 2)number of questions :totalQuestions 3)categories as array :"categories"

POST '/questions'

-INsert a question in the database, it takes the question, answer, category amd difficulty and inserts it in the database
-request body: json fromat for 1)question 2)answer 3)category 4)difficulty
-returns :None


DELETE '/questions/'<int:question>'

-Delete the question with the requested ID from database
-request argument: only requires the ID to be passed in the url of delete method
-returns: None


POST '/questions/search'

-Search in case insensitive manner for  questions with a  given a certain keyword, it returns all matching questions which has the string provided
-request Body: searchTerm
-return:all matching questions :"questions", total number of questions :"totalQuestions"

GET '/categories/<int:category_id>/questions'


-provide all questions with a certain category 
-request argument: the id of category attached  needed in the url for example:/categories/1/questions
-return : questions for the category provided :questions, current category :currentCategory, total questions: totalQuestions


POST '/quizzes'

-provide quizzes questions according to category provided andprevious questions IDS, it provde a new question that is nnot present in previous questions and has the
same category as the one provided
-request body:
    previous_questions:list of IDs of past questions in this play instance
    quiz_category: requested category of questions
-return: 
    question: return a questions of the requested category and that wasnt found in previous questions.    



To run the tests, run
```
replace line "migrate = Migrate(app,db)" in models.py with "db.create_all()"
dropdb trivia_test
createdb trivia_test
python test_flaskr.py (to setup tables)
psql trivia_test < trivia.psql
(this is the test running)
python test_flaskr.py
```