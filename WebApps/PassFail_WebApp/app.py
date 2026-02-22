import streamlit as st
import os
import sys
import random
import numpy as np

# -------- PATH FIX (IMPORTANT) ----------
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(os.path.join(project_root, "Pass_Fail_Predictor"))

from model import PassFailModel

# -------- PAGE CONFIG ----------
st.set_page_config(page_title="Academic Analyzer", layout="wide")

# -------- INSPIRATIONAL QUOTES ----------
inspirational_quotes = [
    "Dream is not what you see in sleep. Dream is something that does not let you sleep. — A.P.J Abdul Kalam",
    "Excellence is a continuous process and not an accident. — A.P.J Abdul Kalam",
    "Small aim is a crime; have great aim. — A.P.J Abdul Kalam",
    "Success is when your signature becomes an autograph. — A.P.J Abdul Kalam",
    "Learning gives creativity. Creativity leads to thinking. Thinking provides knowledge."
]

fail_quotes = [
    "Every expert was once a beginner. Keep going.",
    "Failure is not the opposite of success, it is part of it.",
    "Progress takes time. Don’t give up.",
    "You are capable of more than you think.",
    "Hard work today creates confidence tomorrow."
]

# -------- CSS DESIGN ----------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&family=Poppins:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Background */
.stApp {
    background: radial-gradient(circle at top, #14213d, #0b132b);
}

/* Heading */
.main-title {
    font-family: 'Playfair Display', serif;
    font-size: 48px;
    font-weight: 700;
    text-align: center;
    background: linear-gradient(90deg, #cdb4db, #ffc8dd);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.sub-title {
    text-align: center;
    font-size: 18px;
    color: #cbd5e1;
    margin-bottom: 30px;
}

/* Quote Box */
.quote-box {
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(12px);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    font-size: 18px;
    color: #e2e8f0;
    margin-bottom: 40px;
    animation: fadein 1s ease-in-out;
}

/* Button Glow */
.stButton > button {
    background: linear-gradient(90deg, #7b2cbf, #9d4edd);
    color: white;
    border-radius: 30px;
    padding: 12px 30px;
    border: none;
    font-weight: 600;
    transition: 0.3s ease;
}

.stButton > button:hover {
    box-shadow: 0 0 20px rgba(157,78,221,0.6);
    transform: translateY(-2px);
}

/* Result Cards */
.result-pass {
    background: linear-gradient(145deg, #0f5132, #198754);
    padding: 35px;
    border-radius: 20px;
    color: white;
    text-align: center;
    animation: fadein 0.8s ease-in-out;
    box-shadow: 0 0 25px rgba(25,135,84,0.4);
}

.result-fail {
    background: linear-gradient(145deg, #3a0ca3, #4361ee);
    padding: 35px;
    border-radius: 20px;
    color: white;
    text-align: center;
    animation: fadein 0.8s ease-in-out;
    box-shadow: 0 0 25px rgba(67,97,238,0.4);
}

@keyframes fadein {
    from {opacity: 0; transform: translateY(15px);}
    to {opacity: 1; transform: translateY(0);}
}

</style>
""", unsafe_allow_html=True)

# -------- TITLE ----------
st.markdown('<div class="main-title">🎓 Academic Pass / Fail Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Machine Learning + Academic Rule-Based Evaluation</div>', unsafe_allow_html=True)

# -------- DYNAMIC QUOTE ----------
st.markdown(f'<div class="quote-box">📖 {random.choice(inspirational_quotes)}</div>', unsafe_allow_html=True)

# -------- LOAD MODEL ----------
@st.cache_resource
def load_model():
    model_obj = PassFailModel(os.path.join(project_root, "Pass_Fail_Predictor", "students.csv"))
    model_obj.load_data()
    model_obj.train_model()
    return model_obj

model_obj = load_model()

# -------- INPUTS ----------
col1, col2, col3 = st.columns(3)

with col1:
    math = st.number_input("Math", 0, 100, 50)

with col2:
    reading = st.number_input("Reading", 0, 100, 50)

with col3:
    writing = st.number_input("Writing", 0, 100, 50)

# -------- ANALYZE BUTTON ----------
if st.button("Analyze Result"):

    average = (math + reading + writing) / 3
    prediction = model_obj.predict(math, reading, writing)

    if prediction == "Pass":
        st.markdown(f"""
        <div class="result-pass">
            <h2>🏆 CONGRATULATIONS!</h2>
            <p>You have successfully cleared all academic conditions.</p>
            <p><b>Average Score:</b> {average:.2f}</p>
        </div>
        """, unsafe_allow_html=True)

        st.toast("Excellent Performance! Keep shining 🌟")

    else:
        quote = random.choice(fail_quotes)

        st.markdown(f"""
        <div class="result-fail">
            <h2>Better Luck Next Time!</h2>
            <p>⚠ Keep Moving Forward</p>       
            <p>{quote}</p>
            <p><b>Average Score:</b> {average:.2f}</p>
        </div>
        """, unsafe_allow_html=True)

        st.toast("This is not the end. You can improve 💪")