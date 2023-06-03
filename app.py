import os
import openai
import gradio as gr

#if you have OpenAI API key as an environment variable, enable the below
#openai.api_key = os.getenv("OPENAI_API_KEY")

#if you have OpenAI API key as a string, enable the below
openai.api_key = "your API key put here.."

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.3,
    max_tokens=3000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history

block = gr.Blocks()



with block:

    gr.Markdown(
        """   <center>     <h1>Personalized Chatbot for Job Support</h1></center><br> """ )
    message=gr.Dropdown(
            ["How to join Microsoft employe give a step by step procedure","How to join Google employe give a step by step procedure", "How to join Uber employe give a step by step procedure", "How to join TCS employe give a step by step procedure","How to join Wipro employe give a step by step procedure", "How to join Sumsung employe give a step by step procedure","Other company"], label="Select company ", info="")
    # submit = gr.Button("SEND")
    
    # message= message+"and give step bt step procedeure"
    
    with gr.Row():
        submit = gr.Button("SEND")
        clear= gr.Button("CLEAR")
    
    chatbot = gr.Chatbot()
    state = gr.State()
    
    # submit = gr.Button("SEND")
    
    submit.click(chatgpt_clone, inputs=[message , state], outputs=[chatbot, state])
    clear.click(lambda: None, None, chatbot, queue=False)


block.launch(debug = True)
