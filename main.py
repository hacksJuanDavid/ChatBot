import streamlit as st
from Logic.Chatbot import Chatbot

# Create a funtion main 
def main():

    # Create an instance of the class Chatbot
    chatbot = Chatbot()

    # Call the function chatWithBot
    chatbot.chatWithBot()

# Call the function main
main()