import streamlit as st

col1, col2 = st.columns([0.8, 0.2])
with col1:
    st.header("Leaf Mold")
with col2:
    if st.button("Move to home"):
        st.switch_page("app.py")
st.image("tomato_diseases/tomato leaf disease images/Leaf_Mold.jpeg")
st.subheader("Precautions:")
st.markdown("""
**Prevention:** Ensure good ventilation in greenhouses, avoid high humidity, and use resistant tomato varieties.

**Treatment:** Apply fungicides such as copper sprays, remove infected leaves, and improve air circulation.
""")