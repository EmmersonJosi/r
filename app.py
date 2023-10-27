import streamlit as st
import joblib

# Load the saved model
model_filename = "sentiment_model.pkl"
loaded_model = joblib.load(model_filename)

st.title("Sentiment Analysis App")

user_input = st.text_area("Enter a sentence:")
if st.button("Analyze"):
    prediction = loaded_model.predict([user_input])
    st.write("Predicted Sentiment:", prediction[0])



