import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Pass the api key
openai.api_key = os.getenv("OPENAI_API_KEY")

messages = []
messages.append({
  "role": "system",
  "content": "You are a quiz. Present the user with a multiple-choice question to practice for a python interview, they have to respond by typing a,b,c,d or e. Wait until the user responds before presenting a new question. You talk perfectly in Spanish"
})
while True:
  #send the api call
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
  )
  # Display responses in console
  print(response.choices[0].message.content)

  # Expanding the conversation
  messages.append(response.choices[0].message)

  # Capture user input
  user_input = input("Enter your answer: ")

  # quit loop if uses presses "q"
  if user_input == "q":
    exit()

  # prompt preparation
  messages.append({"role":"user", "content": user_input})