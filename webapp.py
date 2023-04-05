import openai
import gradio as gr
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

def respond(history, new_message):
  # Add user input to messages
  messages.append({"role": "user", "content": new_message})
  # API Call
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
  )
  # Obtain response text
  assistant_message = response.choices[0].message
  messages.append(assistant_message)
  return history + [[new_message, assistant_message.content]]

with gr.Blocks() as my_bot:
  chatbot = gr.Chatbot()
  user_input = gr.Text()

  user_input.submit(respond, [chatbot, user_input], chatbot)
  user_input.value = ""

my_bot.launch()