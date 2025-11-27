# 🤖 Django + Gemini RAG Chatbot

A powerful, full-stack Generative AI Chatbot capable of processing multiple PDF documents and
answering questions based on their content (RAG). Built with Django for a secure backend and React
for a responsive, streaming frontend.
```
Demo Video link: https://youtu.be/c4BgwxHOU70
```

## ✨ Features

```
📄 Multi-PDF RAG System: Upload multiple PDF files simultaneously to create a dynamic
knowledge base.
🧠 Context-Aware AI: Uses Retrieval Augmented Generation (RAG) to answer questions strictly
based on uploaded documents.
🔒 Secure Architecture: API Keys are stored securely on the Django backend, never exposed to
the client.
⚡ Real-time Streaming UI: Typewriter effect for AI responses using React state management.
📝 Markdown Support: Renders code blocks, lists, bold text, and tables beautifully.
🐳 Docker Ready: Fully containerized and optimized for deployment on Hugging Face Spaces.
📱 Responsive Design: Mobile-friendly interface built with Tailwind CSS.
```
## 🛠 Tech Stack

Frontend
React 18: (Standalone mode) for interactive UI state management.
Tailwind CSS: For modern, responsive styling.
PDF.js: Client-side PDF parsing and text extraction to reduce server load.
Marked.js & DOMPurify: Safe Markdown rendering.

Backend
Django: Robust Python web framework handling API requests and security.
Google Generative AI SDK: Interface for the Gemini Pro model.
Gunicorn: Production-grade WSGI HTTP Server.

DevOps
Docker: Multi-stage build for consistent deployment.
Hugging Face Spaces: Target deployment platform.

## 🚀 Installation & Local Setup


Prerequisites
Python 3.9+
A Google Gemini API Key (Get one here)

1. Clone the Repository

```
git clone https://github.com/saurabhkumar9901/My-chat
cd My-chat
```
2. Create Virtual Environment

```
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```
3. Install Dependencies

```
pip install -r requirements.txt
```
4. Set Environment Variables
Create a .env file in the root directory:

```
DEBUG=FALSE
SECRET_KEY=django-insecure-_^m%a!50&cs_=+w533q6s1d(rchcmqmnv7o5ax3idmsin%rnbt
GEMINI_API_KEY=your-gemini-key
```
5. Run the Server

```
python manage.py runserver
```
Access the app at [http://127.0.0.1:8000.](http://127.0.0.1:8000.)

## 🐳 Docker Usage

Build the Image


You can bake your configuration into the build (not recommended for public repos) or inject it at
runtime.

```
# Build passing arguments (for local testing)
docker build \
--build-arg API_KEY=your-gemini-key \
--build-arg SECRET_KEY=django-insecure-_^m%a!50&cs_=+w533q6s1d(rchcmqmnv7o5ax3idmsin%rnbt \
--build-arg DEBUG=False \
-t mychatbot.
```
Run the Container
Map local port 8000 to container port 7860 (Hugging Face default).

```
docker run -p 8000:7860 mychatbot
```
## 🌐 Deployment (Hugging Face Spaces)

1. Create a new Space on Hugging Face.
2. Select Docker as the SDK.
3. Upload the contents of this repository.
4. Go to Settings > Variables and secrets.
5. Add a new Secret:
    Key: GEMINI_API_KEY
    Value: Your Actual Google Key
6. Wait for the build to finish. Your chatbot is live!

## 📂 Project Structure

```
gemini-django-chatbot/
│
├── Dockerfile 
├── requirements.txt 
├── manage.py 
├── .env 
│
├── mychatbot/ 
│ ├── settings.py 
│ ├── urls.py 
│ ├── views.py 
│ └── wsgi.py 
│
└── templates/ 
  └── index.html 
```
## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the Apache 2.0 License.
