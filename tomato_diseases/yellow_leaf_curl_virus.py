import streamlit as st
col1, col2 = st.columns([0.8, 0.2])
with col1:
    st.header("Tomato Yellow Leaf Curl Virus")
with col2:
    if st.button("Move to home"):
        st.switch_page("app.py")
st.image("tomato_diseases/tomato leaf disease images/Tomato_Yellow_Leaf_Curl_Virus.jpeg")
st.subheader("Precautions:")
st.markdown("""
**Prevention:** Use resistant varieties, control whiteflies with neem oil, and install insect netting.

**Treatment:** There is no cure, so remove infected plants to prevent spread and use reflective mulches to deter whiteflies.
""")