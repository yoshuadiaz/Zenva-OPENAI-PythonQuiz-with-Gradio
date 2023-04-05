# OpenAI Chatbot
This project contains two files, app.py and webapp.py, that utilize OpenAI to create a chatbot for practicing multiple-choice Python interview questions. Both files use the OpenAI API and the dotenv library to authenticate API access.

## Requirements
- Python 3.x
- OpenAI API key
- Python libraries: openai, dotenv, gradio (for webapp.py only)

## Setup
- Clone the repository.
- Install the required dependencies with pip install -r requirements.txt.
- Create a .env file and add your OpenAI API key as OPENAI_API_KEY=<your-api-key>.

## Usage
**app.py**
- Run app.py with python app.py.
- The chatbot will display a message containing the instructions for the quiz.
- The user should respond with a, b, c, d, or e to answer the question.
- The chatbot will respond with feedback on the user's response and present a new question.
- To quit the program, enter 'q' instead of a multiple-choice answer.

**webapp.py**
- Run webapp.py with python webapp.py.
- A web page will open in the browser displaying the chatbot interface.
- Follow the same instructions as for app.py.

### Note
Both the scripts use the same GPT-3 model and talk perfectly in Spanish.



