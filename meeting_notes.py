import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("📋 Meeting Notes Summarizer")
st.write("Paste your meeting transcript below and get a clean summary instantly.")

# Transcript Input Box
transcript = st.text_area("📝 Enter Meeting Transcript", height=250)

# Button Click
if st.button("Summarize Meeting"):

    if transcript.strip() == "":
        st.warning("⚠️ Please enter a transcript first.")
    else:
        with st.spinner("Summarizing... Please wait ⏳"):

            # Prompt for Gemini
            prompt = f"""
            Summarize this meeting with headings:

            ## Key Decisions
            ## Action Items
            ## Important Dates

            Transcript:
            {transcript}
            """

            # Generate Response
            response = model.generate_content(prompt)

            # Display Output in Markdown
            st.subheader("✅ Meeting Summary")
            st.markdown(response.text)
