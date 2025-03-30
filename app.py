import streamlit as st
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

st.title('Welcome to Farm Lab')
st.subheader('This is a mobile lab where you test the quality of your plant using your phone camera.', divider='green')
# st.divider()

if "image" not in st.session_state:
    st.session_state.image = None

action = st.radio("Choose an action:", ["None", "Take a Picture", "Upload a Picture"])

# if action == "None":
#     st.rerun()
if action == "Take a Picture":
    enable = st.checkbox("Enable camera")
    img = st.camera_input("Take a picture", disabled=not enable)
    if img is not None:
        st.session_state.image = img

elif action == "Upload a Picture":
    img = st.file_uploader("Click to upload", type=['jpg', 'jpeg', 'png'])
    if img is not None:
        st.session_state.image = img  # Save image to session state
leaf_labels = ['Tomato___Bacterial_spot',
  'Tomato___Early_blight',
  'Tomato___Late_blight',
  'Tomato___Leaf_Mold',
  'Tomato___Septoria_leaf_spot',
  'Tomato___Spider_mites',
  'Tomato___Target_Spot',
  'Tomato___Yellow_Leaf_Curl_Virus',
  'Tomato___Tomato_mosaic_virus',
  'Tomato___healthy']
if st.session_state.image is not None:
    img = st.session_state.image
    img = Image.open(img).convert("RGB")
    img_resized = tf.image.resize(img, (256, 256))
    img_array = image.img_to_array(img_resized)
    img_batch = np.expand_dims(img_array, axis=0)
    model = load_model('tomato_leaf_disease_classification_model_vgg16.keras')
    y_pred = model.predict(img_batch)

    pred_label = leaf_labels[np.array(y_pred).argmax()]

    col1 , col2 = st.columns(2)
    with col1:
        if pred_label == 'Tomato___healthy':
            st.markdown(
                """
                <div style="
                    display: inline-block;
                    background-color: #d2ffd2;
                    color: green;
                    padding: 5px 10px;
                    border-radius: 5px;
                    font-size: 16px;
                    font-weight: bold;
                ">
                    ✅ The leaf is healthy
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style="
                    display: inline-block;
                    background-color: #ffe5a9;
                    color: orange;
                    padding: 5px 10px;
                    border-radius: 5px;
                    font-size: 16px;
                    font-weight: bold;
                ">
                    🚨 {pred_label}
                </div>
                """,
                unsafe_allow_html=True
            )
        with col2:
            if st.button('Read Precautions and Treatment'):
                st.switch_page(f"tomato_diseases/{pred_label.lower().replace("tomato___", '')}.py")
            print(np.round(y_pred*100))



