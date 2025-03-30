import streamlit as st

col1, col2 = st.columns([0.8, 0.2])
with col1:
    st.header("Healthy")
with col2:
    if st.button("Move to home"):
        st.switch_page("app.py")
st.image("tomato_diseases/tomato leaf disease images/healthy.jpeg")
st.subheader("Precautions:")
st.markdown("""
**Maintenance:** Regularly inspect for pests and diseases, ensure proper watering, and use organic fertilizers.
""")