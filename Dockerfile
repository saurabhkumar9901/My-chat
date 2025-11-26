# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# -----------------------------------------------------------
# METHOD 2: BUILD ARGUMENTS
# -----------------------------------------------------------
# 1. Define the arguments (passed via --build-arg)
ARG API_KEY
ARG SECRET_KEY
ARG DEBUG

# 2. Persist them as Environment Variables for Django
# Note: We map API_KEY to GEMINI_API_KEY to match your views.py
ENV API_KEY=$API_KEY
ENV SECRET_KEY=$SECRET_KEY
ENV DEBUG=$DEBUG
# -----------------------------------------------------------

# Copy requirements first to leverage Docker cache
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir --no-deps -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Create directory for static files
RUN mkdir -p staticfiles

# Run Django's collectstatic to organize CSS/JS files
# This step requires SECRET_KEY to be present in the env
RUN python manage.py collectstatic --noinput

# Hugging Face Spaces listens on port 7860 by default
EXPOSE 7860

# Start the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "mychatbot.wsgi:application"]