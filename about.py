import streamlit as st
st.title("Hello")
pages = {
    "Disease": [
        st.Page("tomato_diseases/bacterial_spot.py", title="Bacterial Spot", icon=":material/microbiology:"),
        st.Page("tomato_diseases/early_blight.py", title="Early Blight", icon=":material/microbiology:"),
    ],
}