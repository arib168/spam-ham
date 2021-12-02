import streamlit as st
import joblib 
st.title('SPAM HAM CLASSIFICATION')         #title for the webapp
text_model = joblib.load('spam-ham')        #load the model using joblib
ip = st.text_input('Enter your message :')  #user input in streamlit 
op = text_model.predict([ip])               #predict if the written message is spam or ham 
if st.button('Predict'):                    #create a button called as predict 
  st.title(op[0])                           #if the button is pressed, then print if the msg is spam or ham 