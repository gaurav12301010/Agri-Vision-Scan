import streamlit as st
col1, col2 = st.columns(2)

col1, col2 = st.columns([0.8, 0.2])
with col1:
    st.header("Bacterial Spot")
with col2:
    if st.button("Move to home"):
        st.switch_page("app.py")
st.image("tomato_diseases/tomato leaf disease images/Bacterial_spot.jpeg")
st.subheader("Precautions:")

multi = '''
**Prevention:** Use certified disease-free seeds, rotate crops, and avoid overhead watering.

**Treatment:** Apply copper-based fungicides, remove infected leaves, and use bacteriophage-based sprays.
'''
st.markdown(multi)