import streamlit as st

col1, col2 = st.columns([0.8, 0.2])
with col1:
    st.header("Spider Mites (Two-spotted Spider Mite)")
with col2:
    if st.button("Move to home"):
        st.switch_page("app.py")
st.image("tomato_diseases/tomato leaf disease images/Spider_mites Two-spotted_spider_mite.jpeg")
st.subheader("Precautions:")
st.markdown("""
**Prevention:** Introduce beneficial insects like ladybugs and keep plants well-watered.

**Treatment:** Spray with neem oil or insecticidal soap, increase humidity, and remove infested leaves.
""")