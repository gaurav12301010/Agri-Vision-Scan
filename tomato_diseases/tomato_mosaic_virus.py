import streamlit as st

col1, col2 = st.columns([0.8, 0.2])
with col1:
    st.header("Tomato Mosaic Virus")
with col2:
    if st.button("Move to home"):
        st.switch_page("app.py")
st.image("tomato_diseases/tomato leaf disease images/Tomato_mosaic_virus.jpeg")
st.subheader("Precautions:")
st.markdown("""
**Prevention:** Wash hands and tools before handling plants, control aphids, and remove infected plants.

**Treatment:** No direct cure; remove and destroy infected plants and disinfect tools to prevent further spread.
""")