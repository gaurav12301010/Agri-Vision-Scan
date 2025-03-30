import streamlit as st
multi = '''
# About Agri Vision Scan

## Introduction
Welcome to **Agri Vision Scan**, an AI-powered solution designed to help farmers and agricultural enthusiasts identify and manage tomato plant diseases efficiently. Using advanced deep learning techniques, our app can classify various diseases affecting tomato leaves and provide users with prevention and treatment recommendations.

## How It Works
Our app utilizes a Convolutional Neural Network (CNN) model based on the pre-trained VGG16 architecture, fine-tuned on a dataset of approximately 10,000 images from Kaggle. With an impressive accuracy of 93% on the test dataset, our model effectively predicts the type of disease affecting the tomato plant from an uploaded image.

### Key Features:
- **Image Upload & Camera Support**: Users can either capture a live photo or upload an image of a tomato leaf.
- **Disease Classification**: The app identifies the disease from one of the following categories:
  - Bacterial Spot
  - Early Blight
  - Late Blight
  - Leaf Mold
  - Septoria Leaf Spot
  - Spider Mites (Two-spotted Spider Mite)
  - Target Spot
  - Tomato Yellow Leaf Curl Virus
  - Tomato Mosaic Virus
  - Healthy Leaf
- **Prevention & Treatment Guide**: Once a disease is identified, users receive expert advice on how to prevent and treat the issue.
- **User-Friendly Interface**: Built using Streamlit, our app offers a seamless and interactive experience.

## Our Mission
Our goal is to empower farmers and gardeners with AI-driven tools to detect and manage plant diseases early. By leveraging machine learning and image processing, we aim to minimize crop losses and promote sustainable agriculture.

## Future Vision
We plan to scale **Agri Vision Scan** to detect diseases in various plants beyond tomatoes. Our broader vision is to create AI-powered solutions for multiple agricultural challenges, ensuring farmers have access to cutting-edge technology to protect their crops.

## Get Started
Try out **Agri Vision Scan** today and take a step towards smarter farming. Your feedback and suggestions are valuable in helping us improve and expand our platform!

For more information and updates, stay connected with us.


'''

st.markdown(multi)
