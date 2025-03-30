import streamlit as st

col1, col2 = st.columns([0.8, 0.2])
with col1:
    st.header("Septoria Leaf Spot")
with col2:
    if st.button("Move to home"):
        st.switch_page("app.py")
st.image("tomato_diseases/tomato leaf disease images/Septoria_leaf_spot.jpeg")
st.subheader("Precautions:")
st.markdown("""
**Prevention:** Use mulch to prevent soil splashes, rotate crops, and water at the base of plants.

**Treatment:** Apply fungicides containing chlorothalonil or copper, prune infected leaves, and remove debris from around the plant.
""")