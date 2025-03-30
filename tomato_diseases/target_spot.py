import streamlit as st

col1, col2 = st.columns([0.8, 0.2])
with col1:
    st.header("Target Spot")
with col2:
    if st.button("Move to home"):
        st.switch_page("app.py")
st.image("tomato_diseases/tomato leaf disease images/Target_Spot.jpeg")
st.subheader("Precautions:")
st.markdown("""
**Prevention:** Avoid overhead watering and maintain proper plant spacing.

**Treatment:** Apply copper-based fungicides, remove infected leaves, and improve ventilation.
""")