# ------------  app.py  -----------------
import streamlit as st
import openai

# Streamlit Cloud will inject the key you store in its Secrets tab
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="RoomGenie", layout="centered")
st.title("🏠 RoomGenie – AI Interior Designer")
st.write(
    "⬆️ Upload an image of your room (optional)  →  "
    "💬 Describe the style you want  →  ✨ Get an AI-generated design!"
)

uploaded = st.file_uploader("Upload room photo (optional)", type=["jpg", "jpeg", "png"])
prompt   = st.text_input(
    "Describe the interior style you want",
    placeholder="e.g. minimalist boho bedroom with warm lighting"
)

if st.button("Generate AI Design"):
    if not prompt.strip():
        st.warning("Please enter a style description.")
        st.stop()

    with st.spinner("Generating with DALL·E 3…"):
        try:
            response = openai.images.generate(
                model   = "dall-e-3",
                prompt  = prompt,
                size    = "1024x1024",
                n       = 1,
                quality = "standard",
            )
            url = response.data[0].url
        except Exception as e:
            st.error(f"OpenAI error → {e}")
            st.stop()

    if uploaded:
        st.image(uploaded, caption="Your room", use_column_width=True)

    st.image(url, caption="AI-generated design", use_column_width=True)

    st.subheader("🛒 Suggested products")
    st.markdown("- [Wall art](https://www.amazon.in/s?k=wall+art)")
    st.markdown("- [Accent chair](https://www.amazon.in/s?k=accent+chair)")
    st.markdown("- [Warm floor lamp](https://www.amazon.in/s?k=floor+lamp)")
