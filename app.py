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

# 🌐 2. Sidebar Branding & Upsell Funnel
with st.sidebar:
    st.markdown("## 🌐 Need a Landing Page?")
    st.write(
        "Great ad copy deserves a high-converting website. We design custom, "
        "lightning-fast websites and landing pages for local service businesses."
    )
    st.link_button(
        "👉 Book a Web Design Consultation", 
        url="https://www.linkedin.com/company/shelsun-tech",
        use_container_width=True
    )
    st.divider()
    st.caption("Powered by Shelsun Tech © 2026")

# Title Setup
st.title("🚀 Shelsun Tech — Elite US Copywriter AI")
st.caption("Generate high-converting, localized direct-response ad copies in 3 seconds.")

# 🔑 3. Secure API Key Management
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    api_key_input = st.text_input("Enter your Gemini API Key to test:", type="password")
    if api_key_input:
        genai.configure(api_key=api_key_input)

# ✍️ 4. User Input Dashboard
st.write("---")
niche_input = st.text_input("📍 Enter Client Niche & Target Location:", placeholder="e.g., HVAC Repair in Phoenix Arizona")

# New Platform Dropdown Selection
platform = st.selectbox(
    "📱 Select Target Ad Platform:",
    [
        "Facebook & Instagram Ads (Visual Feed)", 
        "Google Search Ads (Text-Only / High Intent)", 
        "LinkedIn Ads (Professional / B2B Audience)"
    ]
)

# 🧠 5. Dynamic Platform Logic Setup
platform_instructions = ""
if "Facebook" in platform:
    platform_instructions = (
        "Format the ad perfectly for Facebook and Instagram feeds. Use a highly engaging, emotional tone. "
        "Include natural, scroll-stopping emojis, and a compelling, narrative-driven primary text section."
    )
elif "Google" in platform:
    platform_instructions = (
        "Format the ad perfectly for Google Search text ads. STRICTLY OMIT ALL EMOJIS. "
        "Instead of st paragraphs, structure the output precisely as:\n"
        "Headline 1 (Max 30 chars), Headline 2 (Max 30 chars), Headline 3 (Max 30 chars)\n"
        "Description 1 (Max 90 chars), Description 2 (Max 90 chars).\n"
        "Focus heavily on hyper-local keywords and high buyer intent."
    )
elif "LinkedIn" in platform:
    platform_instructions = (
        "Format the ad for a professional B2B audience on LinkedIn. Use an executive, high-authority tone. "
        "Limit emoji usage significantly. Focus heavily on business value propositions, ROI, dependability, and professional case metrics."
    )

# 🚀 6. Execute Generation
if st.button("Generate Premium Ad Copy") and niche_input:
    with st.spinner("Engineering high-converting copy matrix..."):
        try:
            model = genai.GenerativeModel(
                model_name="gemini-3.1-flash-lite",
                generation_config={"temperature": 0.3},
                system_instruction=(
                    f"You are an elite, high-ticket US Direct-Response Copywriter. "
                    f"Your job is to write high-converting ad copy tailored perfectly for local service businesses.\n\n"
                    f"{platform_instructions}\n\n"
                    f"When the user gives you a business niche and location, you must instantly reply with exactly three items formatted cleanly:\n"
                    f"1. 🔥 THE HOOK: A punchy, single-sentence headline that stops a user from scrolling or captures immediate search intent.\n"
                    f"2. ✍️ PRIMARY TEXT/BODY: A short, persuasive 3-paragraph description using the AIDA framework (Attention, Interest, Desire, Action). Use conversational American English.\n"
                    f"3. 🎯 CALL TO ACTION (CTA): Tell the customer exactly what to do next.\n\n"
                    f"CRITICAL RULES:\n"
                    f"- Never include conversational introductory text like 'Sure, here is your copy!' or 'Hope this helps!'\n"
                    f"- Start directly with the Hook.\n"
                    f"- Avoid robotic clichés like 'Look no further' or 'Revolutionize your experience.'"
                )
            )
            
            response = model.generate_content(niche_input)
            
            # Display output inside a premium styled text container
            st.success("Ad Copy Generated Successfully!")
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"Configuration Error: Please verify your API setup or inputs. {str(e)}")
