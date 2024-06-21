import streamlit as st 
import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyAGCH5nhbiIuOQgaxWSt8TzyjqN7qjO_BY")
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="Chatbot")
# Gemini uses 'model' for assistant; Streamlit uses 'assistant'

def role_to_streamlit(role):
  if role == "model":
    return "assistant"
  else:
    return role
  
# Add a Gemini Chat history object to Streamlit session state
  
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history = [])

# Display Form Title
st.title("Chat With Tanvi !")

# Display chat messages from history above current input box
for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Accept user's next message, add to context, resubmit context to Gemini
if prompt := st.chat_input("I possess a well of knowledge. What would you like to know?"):
    # Display user's last message
    st.chat_message("user").markdown(prompt)
    
    # Send user entry to Gemini and read the response
    response = st.session_state.chat.send_message(prompt) 
    
    # Display last 
    with st.chat_message("assistant"):
        st.markdown(response.text)

       
       