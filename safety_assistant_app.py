import streamlit as st
import openai

# Initialize OpenAI client using your secret API key
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# --- Streamlit Page Setup ---
st.set_page_config(page_title="ClearPath Safety Assistant", layout="wide")
st.title("🛡️ ClearPath Safety Assistant")

# --- Role Selection ---
mode = st.radio("Choose your role:", ["Client (Simple Answers)", "Consultant (Expert Tools)"])

# --- User Input ---
user_input = st.text_area("Enter your safety question or task:")

# --- Get Answer ---
if st.button("Get Answer") and user_input:
    with st.spinner("Thinking..."):
        if mode == "Client (Simple Answers)":
            system_prompt = (
                "You are a friendly workplace safety coach for small business owners. "
                "Explain answers in plain language. Use examples, simple checklists, and avoid technical terms."
            )
        else:
            system_prompt = (
                "You are a senior EHS consultant providing expert-level guidance. "
                "Respond with accurate information, cite OSHA regulations or sources when possible, "
                "and provide actionable compliance tips."
            )

        try:
            # Generate response using GPT
            chat_response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.7
            )

            # Display the response
            st.success("✅ Response:")
            st.write(chat_response.choices[0].message.content)

        except Exception as e:
            st.error(f"Error: {e}")

