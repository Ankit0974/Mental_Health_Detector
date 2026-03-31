import streamlit as st
import requests

# Page config
st.set_page_config(page_title="Mental Health Risk Detector", layout="centered")

st.title("🧠 Mental Health Risk Detector")
st.write("Enter your thoughts and get a risk assessment (AI-based)")

# Input box
user_input = st.text_area("Enter text here:", height=150)

# Button
if st.button("Analyze"):

    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            response = requests.post(
                "http://backend:8000/predict",
                json={"text": user_input}
            )

            result = response.json()

            suicide_prob = result["suicide_probability"]
            risk = result["risk_level"]

            st.subheader("Result")

            # Show probability
            st.write(f"**Suicide Probability:** {suicide_prob:.4f}")

            # Progress bar
            st.progress(float(suicide_prob))

            # Risk display
            if risk == "High Risk":
                st.error(f"⚠️ {risk}")
                st.write("Please consider reaching out to a mental health professional.")
            elif risk == "Moderate Risk":
                st.warning(f"⚠️ {risk}")
            else:
                st.success(f"✅ {risk}")

            # Disclaimer
            st.info(result["note"])

        except Exception as e:
            st.error("Backend not running or connection failed.")