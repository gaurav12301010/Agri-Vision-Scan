import streamlit as st

col1, col2 = st.columns([0.8, 0.2])
with col1:
    st.header("Late Blight")
with col2:
    if st.button("Move to home"):
        st.switch_page("app.py")
st.image("tomato_diseases/tomato leaf disease images/Late_blight.jpeg")
st.subheader("Precautions:")
st.markdown("""
**Prevention:** Use resistant tomato varieties and space plants properly to reduce humidity.

**Treatment:** Remove infected plants immediately, apply fungicides like chlorothalonil or mancozeb, and avoid overhead watering.
""")