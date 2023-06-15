"""This is the main file for the MockInterview dashboard"""

import streamlit as st
from audiorecorder import audiorecorder
import random
from core.speech_to_text import speech_to_text

st.title("Mock Interview Dashboard")

# load data/interview_questions.txt into a list for a dropdown menu
with open("data/interview_questions.txt", "r") as f:
    questions = f.readlines()
    questions = [question.strip() for question in questions]

st.subheader("Select a question")
# add a button to generate a random question and display it
if st.button("Generate Random Question"):
    # write the question with a grey rectangle around it, radius 4, color #3f5369, and 5px padding
    st.session_state["question"] = random.choice(questions)

if "question" in st.session_state:
    st.markdown(
        f'<div style="border-radius: 4px; padding: 5px; background-color: #3f5369; color: white;">{st.session_state["question"]}</div>',
        unsafe_allow_html=True,
    )

st.subheader("Record your response")
audio = audiorecorder("Click to record", "Recording...")
if len(audio) > 0:
    # to play audio in frontend:
    st.audio(audio.tobytes())
    # save audio to a file:
    audio_name = "audio_" + str(random.randint(0, 1000000))
    wav_file = open(f"data/audio_responses/{audio_name}.mp3", "wb")
    wav_file.write(audio.tobytes())

# add a button to "Generate Report" that only appears if audio has been recorded
if st.button("Generate Report"):
    st.write("Generating report...")
    # convert audio to text
    text = speech_to_text(f"data/audio_responses/{audio_name}.mp3")
    st.write(text)
