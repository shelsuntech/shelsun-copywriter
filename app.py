import streamlit as st
import google.generativeai as genai

# 🏢 1. Page Configuration & Styling
st.set_page_config(page_title="Shelsun Tech AI", page_icon="🎯", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0f111a; }
    h1 { color: #00ffcc; font-family: 'Helvetica Neue', sans-serif; }
    div.stButton > button:first-child { background-color: #00ffcc; color: black; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 Shelsun Tech — Elite US Copywriter AI")
st.caption("Generate high-converting, localized direct-response ad copies in 3 seconds.")

# 🔑 2. Secure API Key Management
# In production, we fetch this from Streamlit's secure dashboard secrets
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    # Fallback input for local testing on your Chromebook
    api_key_input = st.text_input("Enter your Gemini API Key to test:", type="password")
    if api_key_input:
        genai.configure(api_key=api_key_input)

# ✍️ 3. User Input Dashboard
st.write("---")
niche_input = st.text_input("📍 Enter Client Niche & Target Location:", placeholder="e.g., HVAC Repair in Phoenix Arizona")

# 🧠 4. Execute the System Instructions Prompt Matrix
if st.button("Generate Premium Ad Copy") and niche_input:
    with st.spinner("Engineering high-converting copy matrix..."):
        try:
            # Replicating your Google AI Studio parameters perfectly
            model = genai.GenerativeModel(
                model_name="gemini-3.1-flash-lite",
                generation_config={"temperature": 0.3},
                system_instruction=(
                    "You are an elite, high-ticket US Direct-Response Copywriter. "
                    "Your job is to write high-converting Facebook and Instagram ad copy for local service businesses.\n\n"
                    "When the user gives you a business niche and location, you must instantly reply with exactly three items formatted cleanly:\n"
                    "1. 🔥 THE HOOK: A punchy, single-sentence headline that stops a user from scrolling on their feed. It must address a local pain point.\n"
                    "2. ✍️ PRIMARY TEXT: A short, persuasive 3-paragraph ad description using the AIDA framework (Attention, Interest, Desire, Action). Use conversational American English and natural emojis.\n"
                    "3. 🎯 CALL TO ACTION (CTA): Tell the customer exactly what to do next (e.g., 'Tap Book Now to secure your slot before the weekend').\n\n"
                    "CRITICAL RULES:\n"
                    "- Never include conversational introductory text like 'Sure, here is your copy!' or 'Hope this helps!'\n"
                    "- Start directly with the Hook.\n"
                    "- Avoid robotic clichés like 'Look no further' or 'Revolutionize your experience.'"
                )
            )
            
            response = model.generate_content(niche_input)
            
            # Display output inside a premium styled text container
            st.success("Ad Copy Generated Successfully!")
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"Configuration Error: Please verify your API setup or inputs. {str(e)}")
