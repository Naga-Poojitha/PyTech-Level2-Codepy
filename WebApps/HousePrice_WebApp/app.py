import streamlit as st
import sys
import os
import random

# ---------------- PATH FIX ----------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../House_Price_Prediction"))
sys.path.append(BASE_DIR)

from model import HousePriceModel

st.set_page_config(page_title="Elite Property AI", layout="wide")

# ---------------- PREMIUM CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(180deg, #0f172a 0%, #0b1120 50%, #111827 100%);
    color: #e5e7eb;
}

/* MAIN HEADING */
.main-title {
    font-family: 'Playfair Display', serif;
    font-size: 60px;
    text-align: center;
    color: #f8fafc;
}

.sub-title {
    text-align: center;
    font-size: 20px;
    color: #94a3b8;
    margin-bottom: 40px;
}

/* HERO GLASS BLOCK */
.hero-block {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 24px;
    padding: 40px;
    backdrop-filter: blur(18px);
    text-align: center;
    margin-bottom: 50px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.5);
}

.hero-line {
    font-size: 28px;
    font-weight: 600;
    color: #f1f5f9;
}

.hero-quote {
    font-size: 16px;
    margin-top: 15px;
    color: #cbd5e1;
    font-style: italic;
}

/* BUTTON */
.big-button > button {
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    border-radius: 40px;
    border: none;
    padding: 14px 40px;
    font-size: 18px;
    font-weight: 600;
    color: white;
    transition: 0.3s ease;
}

.big-button > button:hover {
    box-shadow: 0 0 25px rgba(139,92,246,0.6);
    transform: translateY(-2px);
}

/* RESULT CARD */
.result-card {
    margin-top: 60px;
    background: linear-gradient(135deg, #1e293b, #111827);
    border-radius: 28px;
    padding: 50px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 30px 80px rgba(0,0,0,0.6);
}

.price {
    font-size: 52px;
    font-weight: 700;
    margin-top: 20px;
}

.segment {
    font-size: 22px;
    color: #cbd5e1;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    model = HousePriceModel("../../House_Price_Prediction/kc_house_data.csv")
    model.load_data()
    model.train_model()
    return model

model = load_model()

# ---------------- HEADER ----------------
st.markdown('<div class="main-title">🏠 Elite Property AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">AI-Driven Real Estate Valuation System</div>', unsafe_allow_html=True)

# ---------------- HERO BLOCK CONTENT ----------------
hero_lines = [
    "Where Data Meets Smart Investment.",
    "Redefining Property Intelligence.",
    "Precision Valuation. Strategic Advantage.",
    "AI-Powered Real Estate Insights."
]

hero_quotes = [
    "Buy land, they're not making it anymore. – Mark Twain",
    "Real estate is the best investment in the world. – Andrew Carnegie",
    "Price is what you pay. Value is what you get. – Warren Buffett",
    "In real estate, you make money when you buy. – Barbara Corcoran"
]

st.markdown(f"""
<div class="hero-block">
    <div class="hero-line">{random.choice(hero_lines)}</div>
    <div class="hero-quote">"{random.choice(hero_quotes)}"</div>
</div>
""", unsafe_allow_html=True)

# ---------------- INPUT SECTION ----------------
col1, col2, col3 = st.columns(3)

with col1:
    sqft = st.number_input("Living Area (sqft)", min_value=300, max_value=10000, value=1500)

with col2:
    bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)

with col3:
    bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)

st.markdown('<div class="big-button">', unsafe_allow_html=True)
predict = st.button("Evaluate Property")
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PREDICTION ----------------
if predict:
    price = model.predict(sqft, bedrooms, bathrooms)

    usd = f"${price:,.0f}"
    inr = price * 83

    if inr >= 10000000:
        inr_display = f"₹ {inr/10000000:.2f} Crore"
    else:
        inr_display = f"₹ {inr/100000:.2f} Lakhs"

    if price > 1000000:
        segment = "Ultra Luxury Segment"
    elif price > 500000:
        segment = "Premium Residential Segment"
    else:
        segment = "Growth Investment Segment"

    st.markdown(f"""
    <div class="result-card">
        <div class="segment">{segment}</div>
        <div class="price">{usd}</div>
        <div class="segment">{inr_display}</div>
    </div>
    """, unsafe_allow_html=True)