# Agri Vision Scan

## 🌱 Overview
**Agri Vision Scan** is an AI-powered web application designed to help farmers and agricultural enthusiasts detect and manage tomato leaf diseases early. Using deep learning and computer vision, the model classifies diseases with **93% accuracy** and provides actionable prevention and treatment recommendations.

## APP URL
https://agrivisionscan.streamlit.app/

## 🚀 Features
- **Image Upload & Camera Support**: Users can upload an image or take a picture of a tomato leaf.
- **AI-Powered Disease Classification**: Detects 10 types of tomato leaf conditions, including bacterial and viral infections.
- **Prevention & Treatment Advice**: Offers expert recommendations on managing plant diseases.
- **User-Friendly Interface**: Built using **Streamlit** for a smooth experience.

## 🧠 How It Works
1. **Image Input**: The user uploads or captures an image of a tomato leaf.
2. **AI Model Analysis**: The model (based on **VGG16 & TensorFlow/Keras**) processes the image and classifies the disease.
3. **Results & Solutions**: The app provides disease details and solutions for management and prevention.

## 🏗️ Tech Stack
- **Framework**: Streamlit
- **Machine Learning**: TensorFlow, Keras
- **Model Architecture**: VGG16 (pre-trained on ImageNet)
- **Dataset**: Kaggle Tomato Leaf Disease Dataset (~10,000 images)
- **Deployment**: Streamlit Cloud

## 🔧 Installation
### Prerequisites:
- Python 3.x
- TensorFlow
- Keras
- Streamlit
- OpenCV
- NumPy, Pandas, Matplotlib

### Steps to Run Locally:
1. Clone the repository:
   ```bash
   git clone [Insert GitHub Repo Link]
   cd agri-vision-scan
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```
4. Open the provided local URL in your browser.

## 📂 Dataset
The dataset used for training the model was sourced from Kaggle. You can find it here:
https://www.kaggle.com/datasets/kaustubhb999/tomatoleaf

## 🚀 Future Enhancements
- Expand disease detection to **other plant species**.
- Improve model accuracy and reduce overfitting.
- Integrate multilingual support for better accessibility.
- Develop a **mobile version** for real-time scanning in the field.

## 🤝 Contributing
We welcome contributions! If you’d like to improve the model or add features, feel free to **fork the repo, make changes, and submit a PR**.

## 📬 Contact
For inquiries, collaborations, or feedback, reach out to me:
- LinkedIn: https://www.linkedin.com/in/gauravkumarsaha/
- Email: gauravkumarsaha2216@gmail.com

### ⭐ If you find this project useful, don’t forget to **star** the repository!

#AI #MachineLearning #DeepLearning #AgricultureTech #ComputerVision #FarmTech #AgriVisionScan #Innovation

