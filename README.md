# AI PDF Chatbot using Gemini + RAG

An AI-powered PDF Question Answering Chatbot built using Google Gemini API, Gradio, and Retrieval-Augmented Generation (RAG) concepts.

This application allows users to upload PDF documents and ask questions based on the content of the uploaded file. The chatbot intelligently reads the PDF and provides accurate, context-based answers using Gemini.

Live Deployment:  
https://huggingface.co/spaces/shimanshushrivastava96/ai-pdf-chatbot-gemini

---

## Project Overview

Traditional PDF reading is time-consuming when users need quick answers from large documents.

This project solves that problem by creating an intelligent chatbot that can:

- Upload PDF files
- Understand document content
- Answer questions from the uploaded PDF
- Provide fast and relevant responses
- Improve productivity for document analysis

This project demonstrates practical implementation of:

- Generative AI
- LLM Integration
- Document Understanding
- Prompt Engineering
- API Integration
- AI Product Deployment

---

## Features

### PDF Upload Support
Users can upload PDF files directly into the application.

### Intelligent Question Answering
Users can ask natural language questions from the uploaded PDF.

### Gemini API Integration
Google Gemini processes the document context and generates smart answers.

### Clean Gradio Interface
Simple and user-friendly frontend built using Gradio.

### Live Public Deployment
Deployed on Hugging Face Spaces for public access.

### Recruiter-Friendly AI Project
Production-ready portfolio project for AI/ML roles.

---

## Tech Stack

### Frontend
- Gradio

### Backend
- Python

### AI Model
- Google Gemini 2.5 Flash

### Deployment
- Hugging Face Spaces

### Environment Management
- Python Dotenv

---

## Project Structure

```bash
AI-PDF-Chatbot-LLM-RAG/
│
├── app.py
├── requirements.txt
├── README.md
├── .env (local only)
└── .gitignore
Installation Guide
Step 1: Clone Repository
git clone https://github.com/shimanshushrivastava96/AI-PDF-Chatbot-LLM-RAG.git
cd AI-PDF-Chatbot-LLM-RAG
Step 2: Create Virtual Environment
python -m venv venv

Activate virtual environment:

Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate
Step 3: Install Dependencies
pip install -r requirements.txt
Step 4: Create .env File

Create a .env file in the root folder:

GEMINI_API_KEY=your_actual_gemini_api_key

Important:
Do NOT upload .env to GitHub.

Step 5: Run Application
python app.py

Application will run on:

http://127.0.0.1:7860
Deployment

This project is deployed publicly using:

Hugging Face Spaces

Live App: https://huggingface.co/spaces/shimanshushrivastava96/ai-pdf-chatbot-gemini


This system can be used for:

Resume Analysis
Legal Document Review
Telecom Alarm Troubleshooting Docs
SOP Analysis
Research Paper Understanding
Internal Company Knowledge Base
Policy Document Search

LinkedIn: https://www.linkedin.com/in/shimanshu-shrivastav-3623a7145

GitHub: https://github.com/shimanshushrivastava96

License:- MIT License


Final Note:
This project is built not just as a demo, but as a practical production-ready AI application showcasing real-world implementation of LLMs and RAG systems for solving business problems.
