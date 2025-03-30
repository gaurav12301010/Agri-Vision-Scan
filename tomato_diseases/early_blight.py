import streamlit as st

col1, col2 = st.columns([0.8, 0.2])
with col1:
    st.header("Early Blight")
with col2:
    if st.button("Move to home"):
        st.switch_page("app.py")
st.image("tomato_diseases/tomato leaf disease images/early_blight.jpeg")
st.subheader("Precautions:")
st.markdown("""
**Prevention:** Practice crop rotation, ensure good air circulation, and avoid wetting leaves.

**Treatment:** Use fungicides containing chlorothalonil or copper, prune affected leaves, and apply organic treatments like neem oil.
""")