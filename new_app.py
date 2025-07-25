import streamlit as st
import pickle

# Load model
with open('CPP.pkl', 'rb') as file:
    rf = pickle.load(file)

# Detect dark mode
theme = st.get_option("theme.base")
dark_mode = theme == "dark"

# Color themes
colors = {
    "bg": "#121212" if dark_mode else "#ffffff",
    "text": "#f0f0f0" if dark_mode else "#222222",
    "subtle": "#aaaaaa" if dark_mode else "#555555",
    "highlight": "#00FFB7" if dark_mode else "#2E8B57",
    "danger": "#FF6B6B",
    "card_bg": "#ffffff",  # Universal white for clarity
    "card_text": "#1e1e1e"
}

# Global Style
st.markdown(f"""
    <style>
    html, body, [class*="css"] {{
        font-family: 'Segoe UI', sans-serif;
        background-color: {colors['bg']};
        color: {colors['text']};
    }}
    .main-title {{
        font-size: 3em;
        text-align: center;
        background: linear-gradient(to right, #00c6ff, #0072ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }}
    .card {{
        background-color: {colors['card_bg']};
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        color: {colors['card_text']};
    }}
    </style>
""", unsafe_allow_html=True)

# --- Title
st.markdown("<div class='main-title'>🎓 Campus Recruitment Prediction</div>", unsafe_allow_html=True)

# --- Intro
st.markdown(f"""
<div class="card">
<p style='text-align: justify; font-size: 15px;'>
Campus recruitment is a strategic initiative where organizations connect with fresh graduates from universities for entry-level roles. 
It helps companies tap into young, trainable, and energetic talent pools while providing students early career opportunities.
</p>
<p style='font-size: 13px; color: {colors['subtle']};'>Dataset Source: 
<a href='https://www.kaggle.com/datasets' target='_blank'>Click here</a></p>
</div>
""", unsafe_allow_html=True)

# --- Subheader
st.markdown(f"<h3 style='text-align: center; color: {colors['highlight']}; margin-top: 30px;'>📊 Campus Placement Predictor</h3>", unsafe_allow_html=True)

# --- Inputs
gender = st.selectbox("👤 Select Gender", ("Male", "Female"))
spec = st.selectbox("💼 Select Specialisation", ("Marketing and Finance", "Marketing and HR"))
tech = st.selectbox("📘 Select the Technical Degree", ("Science and Technology", "Others"))
work = st.selectbox("💪 Have Work Experience?", ("No", "Yes"))
ssc = st.slider("📈 SSC Percentage", 0.0, 100.0, 75.0, step=0.1)
hsc = st.slider("🏫 High School Percentage", 0.0, 100.0, 70.0, step=0.1)
dsc = st.slider("🎓 Degree Percentage", 0.0, 100.0, 65.0, step=0.1)
mba = st.slider("📊 MBA Percentage", 0.0, 100.0, 72.0, step=0.1)

# Map inputs
gender_map = {"Male": 1, "Female": 0}
spec_map = {"Marketing and Finance": 1, "Marketing and HR": 0}
tech_map = {"Science and Technology": 1, "Others": 0}
work_map = {"Yes": 1, "No": 0}

inputfeatures = [[
    gender_map[gender],
    spec_map[spec],
    tech_map[tech],
    work_map[work],
    ssc, hsc, dsc, mba
]]

# Predict
if st.button("🔮 Predict Placement Chances"):
    pred_class = rf.predict(inputfeatures)
    pred_prob = rf.predict_proba(inputfeatures)

    label = "✅ Will be Placed" if pred_class[0] == 1 else "❌ Better Luck Next Time"
    prob = pred_prob[0][1] if pred_class[0] == 1 else pred_prob[0][0]
    percent = round(prob * 100, 2)

    # Dynamic suggestions
    if percent < 50:
        advice = "Focus on improving key academic areas and gaining practical experience through internships or projects."
        next_step = "Attend resume workshops, work on communication skills, and take aptitude tests regularly."
    elif 50 <= percent <= 75:
        advice = "You're on the right path! Strengthen your resume with certifications (e.g., Python, Excel, SQL) or mock interviews."
        next_step = "Apply to companies that offer growth-based roles or graduate programs to build experience."
    else:
        advice = "Excellent profile! You're a strong contender for top recruiters in consulting, analytics, or tech."
        next_step = "Start mock interview prep, brush up on group discussion skills, and explore core company test patterns."

    if work == "No" and percent < 70:
        advice += " Since you don't have prior work experience, highlight academic projects and internships in your resume."

    # Result card
    st.markdown(f"""
    <div class="card" style="margin-top: 30px;">
        <h2 style='text-align: center; color: {colors['highlight']}; margin-bottom: 10px;'>🎯 Predicted Result</h2>
        <h4 style='text-align: center; margin-bottom: 15px;'>
            Based on the form inputs, the student: 
            <span style='color: {colors['highlight']}; font-weight: bold;'>{label}</span>
        </h4>
        <p style='text-align: center; font-size: 18px;'>
            Placement Probability: 
            <span style='color: {colors['danger']}; font-weight: bold;'>{percent}%</span>
        </p>
        <hr style='border: 0.5px solid rgba(0,0,0,0.1); margin: 20px 0;'>
        <p style='text-align: center; font-size: 15px;'>
            💡 <strong>Advice:</strong> {advice}<br><br>
            🚀 <strong>Next Step:</strong> {next_step}<br><br>
            <b style='color: {colors['danger']};'>All the Best for your Future!</b>
        </p>
    </div>
    """, unsafe_allow_html=True)