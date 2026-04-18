# AI PDF Chatbot using LLM + RAG

An AI-powered PDF Question Answering Chatbot built using Large Language Models (LLM) and Retrieval-Augmented Generation (RAG).

This project allows users to upload PDF documents and ask questions based on the content of the PDF. The chatbot retrieves relevant context using vector embeddings and semantic search, then generates accurate and meaningful answers using a local LLM.

---

## Project Overview

Traditional chatbots cannot understand PDF content directly.

This project solves that problem by using:

- PDF Processing
- Text Chunking
- Vector Embeddings
- Semantic Search
- Local LLM Response Generation

The system converts PDF content into searchable vector embeddings using FAISS and HuggingFace Embeddings, then retrieves the most relevant information for answering user queries.

---

## Tech Stack

### Programming Language
- Python

### Frameworks & Libraries
- Gradio
- LangChain
- FAISS
- HuggingFace Embeddings
- Sentence Transformers
- Ollama
- PyPDF Loader

### Concepts Used
- Generative AI
- Large Language Models (LLM)
- Retrieval-Augmented Generation (RAG)
- Natural Language Processing (NLP)
- Vector Database
- Semantic Search

---

## Key Features

- Upload PDF files
- Process PDF content
- Ask questions from uploaded PDF
- Semantic Search using Vector Database
- Local LLM Integration using Ollama
- Reset Chat Functionality
- Simple and clean Gradio Interface

---

## Project Structure

```bash
AI-PDF-Chatbot-LLM-RAG/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE

Update professional README
