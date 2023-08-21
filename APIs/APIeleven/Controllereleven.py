from elevenlabs import generate
import os
from dotenv import load_dotenv


# Class to handle the API calls
class Controllereleven:
    # Load the environment variables
    load_dotenv()

    # Eleven API key
    apiKeyEleven = os.environ.get("ELEVEN_API_KEY")

    # Create a function to call the Eleven API
    def callEleven(self, text, voice, model):
        # Call the Eleven API to generate the audio
        audio = generate(
            text=text,
            voice=voice,
            model=model
        )
        
        return audio

