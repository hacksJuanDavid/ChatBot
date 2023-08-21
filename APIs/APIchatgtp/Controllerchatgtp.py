# Importar las bibliotecas necesarias
import openai
import os
from dotenv import load_dotenv

# Clase para manejar las llamadas a la API de OpenAI
class Controllerchatgtp:
    def __init__(self):
        # Cargar las variables de entorno desde el archivo .env
        load_dotenv()
        
        # Clave de la API de OpenAI
        self.apiKeyOpeai = os.environ.get("OPENAI_API_KEY")

        # Establecer la clave de la API para OpenAI
        openai.api_key = self.apiKeyOpeai

    # Función para llamar a la API de OpenAI
    def callOpenAI(self, userPrompt):
        # Crear una variable assistantPrompt con el inicio de la conversación
        assistantPrompt = '''
            The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.
            '''
            
        # Llamar a la API de OpenAI para completar la conversación
        chatCompletion = openai.ChatCompletion.create(
            model="gpt-4", 
            messages=[
                {"role": "assistant", "content": assistantPrompt},
                {"role": "user", "content": userPrompt},
            ])

        # Obtener la respuesta del chatbot desde la respuesta de la API de OpenAI
        response = chatCompletion.get("choices")[0].get("message").get("content")
        return response





    


