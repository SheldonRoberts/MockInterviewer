"""This is the main file for the MockInterview dashboard"""

import streamlit as st
from audiorecorder import audiorecorder
import random

st.title("Mock Interview Dashboard")

# load data/interview_questions.txt into a list for a dropdown menu
with open("data/interview_questions.txt", "r") as f:
    questions = f.readlines()
    questions = [question.strip() for question in questions]


# add a button to generate a random question and display it
if st.button("Generate Random Question"):
    st.write("The question is...")
    st.write(random.choice(questions))

audio = audiorecorder("Click to record", "Recording...")

if len(audio) > 0:
    # to play audio in frontend:
    st.audio(audio.tobytes())

    # save audio to a file:
    audio_name = "audio_" + str(random.randint(0, 1000000))
    wav_file = open(f"data/audio_responses/{audio_name}.mp3", "wb")
    wav_file.write(audio.tobytes())
