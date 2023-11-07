import openai
import gradio as gr
import time
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]



def get_completion_from_messages(input, model="gpt-3.5-turbo", temperature=0.8):
    messages = [
        {'role': 'system', 'content': '너는 자기소개서에 기반하여 질문을 하는 면접관이야.\
                                     만약 전문용어가 있다면 꼬리질문해줘'},
        {"role": "user","content": input }]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    print(111111)
    return response.choices[0].message["content"]






####
#user input
#get completion 통과 시켜서 답변얻음
#이때 역할 분담 및 프롬프트 엔지니어링 진행
####
class Interviewer:
    def __init__(self):
        # Initialize the ChatBot class with an empty history
        self.history = []

    def predict(self, user_input):
        response =get_completion_from_messages(user_input, temperature=0.8)
        return response


inter = Interviewer()
title = "자소서기반 면접 시뮬레이션 chat bot (this template based on Tonic's MistralMed Chat)"
chatbot = gr.Interface(
    fn=inter.predict,
    title=title,
    inputs="text",
    outputs="text",

)

chatbot.launch()