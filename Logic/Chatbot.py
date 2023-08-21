import streamlit as st
from streamlit_chat import message
from APIs.APIchatgtp.Controllerchatgtp import Controllerchatgtp
from APIs.APIeleven.Controllereleven import Controllereleven

# Create a class to handle the chatbot
class Chatbot:

    # Función para generar la respuesta del chatbot y guardar el mensaje del usuario y la respuesta en las listas de sesión
    def onInputChange(self):
        controllerChatgtp = Controllerchatgtp()
        controllerEleven = Controllereleven()

        userInput = st.session_state.user_input

        # Use the user input as a prompt for the chatbot
        if userInput:
            chatBotResponse = controllerChatgtp.callOpenAI(userInput)

            # Generate audio from the chatbot response
            audioPathResponse = controllerEleven.callEleven(chatBotResponse, "Bella", "eleven_monolingual_v1")

            # Append user input and chatbot response (both text and audio) to the session state lists
            st.session_state.past.append(userInput)
            st.session_state.generated.append({'type': 'normal', 'data': chatBotResponse})
            st.session_state.generated.append({'type': 'audio', 'data': audioPathResponse})
            
        # Clear the user input text box after submission
        st.session_state.user_input = ""

    def onBtnClick(self):
        # Clear the past and generated message lists
        del st.session_state.past[:]
        del st.session_state.generated[:]

    # Función para interactuar con el chatbot de manera continua
    def chatWithBot(self):
        st.session_state.setdefault(
            'past', 
            [
                'Hello',
            ]
        )
        st.session_state.setdefault(
            'generated', 
            [   
                {'type': 'normal', 'data': 'Hello my name is BotTest \n'},
            ]
        )
        
        # Display the chatbot title
        st.title("Chat Bot GPT-4")
        # Display subtitle
        st.subheader("Use the text box below to chat with the chatbot.")

        # Display the chatbot description
        chatPlaceholder = st.empty()

        # Display the chatbot input text box
        with chatPlaceholder.container():
            # Get the length of the combined responses (text and audio)
            combined_responses_length = len(st.session_state['generated'])
            
            # Ensure both 'past' and 'generated' lists have the same length
            for i in range(len(st.session_state['past']), combined_responses_length):
                st.session_state['past'].append('')  # Add an empty string for each combined response

            # Loop through the combined responses (text and audio) and display them accordingly
            for i in range(combined_responses_length):
                response = st.session_state['generated'][i]
                
                # Check if the response is of type 'audio' and skip displaying user message if true
                if response['type'] != 'audio':
                    message(st.session_state['past'][i], is_user=True, key=f"{i}_user")

                # Display the chatbot response
                if response['type'] == 'normal':
                    message(response['data'], key=f"{i}", allow_html=True,
                            is_table=True if response['type'] == 'table' else False)
                # Display the chatbot audio response
                elif response['type'] == 'audio':
                    # Display the audio player
                    st.audio(response['data'], format='audio/wav', start_time=0)

        # Display the user input text box
        with st.container():
            # Display the clear message button
            st.button("Clear message", on_click=self.onBtnClick)
            # Get the user input
            st.text_input("User Input:", on_change=self.onInputChange, key="user_input")
            # Display the chatbot description
            st.info("Press the enter key to submit your message a bot.")
           
