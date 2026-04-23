import os
import gradio as gr
from dotenv import load_dotenv
from google import genai

print("step 1: imports done")

load_dotenv()
print("step 2: dotenv loaded")

API_KEY = os.getenv("GEMINI_API_KEY")
print("step 3: api key check")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not found.")

client = genai.Client(api_key=API_KEY)
print("step 4: gemini client created")

MODEL_NAME = "gemini-2.5-flash"


def answer_from_pdf(pdf_file, question, chat_history):
    if chat_history is None:
        chat_history = []

    if not question.strip():
        return chat_history, chat_history, ""

    if pdf_file is None:
        chat_history.append({
            "role": "user",
            "content": question
        })
        chat_history.append({
            "role": "assistant",
            "content": "Please upload a PDF first."
        })
        return chat_history, chat_history, ""

    try:
        uploaded_file = client.files.upload(file=pdf_file.name)

        prompt = f"""
You are a helpful PDF question-answering assistant.

Answer the user's question only from the uploaded PDF.
If the answer is not available in the PDF, say:
I could not find that in the uploaded PDF.

User question:
{question}
"""

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=[uploaded_file, prompt]
        )

        answer = response.text if response.text else "No response generated."

    except Exception as e:
        answer = f"Error: {str(e)}"

    chat_history.append({
        "role": "user",
        "content": question
    })
    chat_history.append({
        "role": "assistant",
        "content": answer
    })

    return chat_history, chat_history, ""


def reset_chat():
    return [], [], "", None


with gr.Blocks(title="AI PDF Chatbot using Gemini") as app:
    gr.Markdown("# AI PDF Chatbot using Gemini + PDF")
    gr.Markdown("Upload a PDF and ask questions from it.")

    pdf_input = gr.File(label="Upload PDF", file_types=[".pdf"])
    chatbot = gr.Chatbot(label="Chat")
    question_box = gr.Textbox(
        label="Ask a question from the PDF",
        placeholder="Type your question here..."
    )

    with gr.Row():
        ask_button = gr.Button("Ask")
        reset_button = gr.Button("Reset")

    state = gr.State([])

    ask_button.click(
        fn=answer_from_pdf,
        inputs=[pdf_input, question_box, state],
        outputs=[chatbot, state, question_box]
    )

    question_box.submit(
        fn=answer_from_pdf,
        inputs=[pdf_input, question_box, state],
        outputs=[chatbot, state, question_box]
    )

    reset_button.click(
        fn=reset_chat,
        inputs=[],
        outputs=[chatbot, state, question_box, pdf_input]
    )

if __name__ == "__main__":
    app.launch()
