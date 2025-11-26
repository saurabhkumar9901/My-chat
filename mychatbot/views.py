import json
import os
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai

# 1. Get your API Key from Google AI Studio (https://aistudio.google.com/)

API_KEY = os.environ.get("API_KEY")

genai.configure(api_key=API_KEY)


def index(request):
    """
    Serves the React Frontend.
    Ensure 'index.html' is inside the 'templates' folder.
    """
    return render(request, 'index.html')

@csrf_exempt
def chat_api(request):
    """
    API Endpoint: /api/chat/
    
    This acts as a secure proxy. It receives the document text from the frontend,
    combines it with the user's question, and sends it to Gemini using the
    server-side API Key.
    """
    if request.method == 'POST':
        try:
            
            data = json.loads(request.body)
            user_message = data.get('message', '')
            documents = data.get('documents', [])
            
            
            combined_context = ""
            if documents:
                combined_context = "You have access to the following document contents:\n\n"
                for doc in documents:
                    name = doc.get('name', 'Unknown')
                    text = doc.get('text', '')
                    safe_text = text[:20000] 
                    
                    combined_context += f"--- START DOCUMENT: {name} ---\n{safe_text}\n--- END DOCUMENT ---\n\n"
            
            
            final_prompt = f"""
            System: You are a helpful AI assistant. Answer the user's question based strictly on the provided document context below.
            If the answer is not in the context, say "I couldn't find that information in the documents."
            
            {combined_context}
            
            User Question: {user_message}
            """
            model = genai.GenerativeModel('gemini-2.5-flash-preview-09-2025')
            response = model.generate_content(final_prompt)
            
            return JsonResponse({'reply': response.text})

        except Exception as e:
            print(f"SERVER ERROR: {e}")
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method. Use POST.'}, status=405)