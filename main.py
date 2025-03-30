import streamlit as st

st.logo('images.jpeg', size="large")
pages = {
    "Home": [
        st.Page("app.py", title="Home", icon=":material/home:"),
        st.Page("about.py", title="About Us", icon=":material/quick_reference:"),
    ],
    "Disease and Precautions": [
    st.Page("tomato_diseases/bacterial_spot.py", title="Bacterial Spot", icon=":material/microbiology:"),
    st.Page("tomato_diseases/early_blight.py", title="Early Blight", icon=":material/microbiology:"),
    st.Page("tomato_diseases/late_blight.py", title="Late Blight", icon=":material/microbiology:"),
    st.Page("tomato_diseases/leaf_mold.py", title="Leaf Mold", icon=":material/microbiology:"),
    st.Page("tomato_diseases/septoria_leaf_spot.py", title="Septoria Leaf Spot", icon=":material/microbiology:"),
    st.Page("tomato_diseases/spider_mites.py", title="Spider Mites (Two-spotted Spider Mite)", icon=":material/microbiology:"),
    st.Page("tomato_diseases/target_spot.py", title="Target Spot", icon=":material/microbiology:"),
    st.Page("tomato_diseases/yellow_leaf_curl_virus.py", title="Tomato Yellow Leaf Curl Virus", icon=":material/microbiology:"),
    st.Page("tomato_diseases/tomato_mosaic_virus.py", title="Tomato Mosaic Virus", icon=":material/microbiology:"),
    st.Page("tomato_diseases/healthy.py", title="Healthy", icon=":material/eco:")
],
}

pg = st.navigation(pages)
pg.run()