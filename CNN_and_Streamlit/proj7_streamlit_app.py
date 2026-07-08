"""
1B - Streamlit App: Intel Image Classification
------------------------------------------------
Name       : Aditya Roshan S (Aadi)
Student ID : 24BAI10227
Program    : B.Tech AI/ML Engineering, VIT Bhopal University

This app loads the CNN model trained in `1A_CNN_Intel_Image_Classification.ipynb`
(saved as `intel_cnn_model.keras`) and lets the user upload an image to get a
predicted scene category out of: buildings, forest, glacier, mountain, sea, street.

Run with:
    streamlit run 1B_streamlit_app.py
"""

import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image

# ---------------------------------------------------------
# Config
# ---------------------------------------------------------
MODEL_PATH = "intel_cnn_model.keras"
IMG_SIZE = (150, 150)
CLASS_NAMES = ["buildings", "forest", "glacier", "mountain", "sea", "street"]

st.set_page_config(page_title="Intel Image Classifier", page_icon="🏞️", layout="centered")


# ---------------------------------------------------------
# Load model (cached so it isn't reloaded on every interaction)
# ---------------------------------------------------------
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model(MODEL_PATH)
    return model


def preprocess_image(image: Image.Image) -> np.ndarray:
    """Resize, convert to array, normalize and add batch dimension."""
    image = image.convert("RGB")
    image = image.resize(IMG_SIZE)
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------
with st.sidebar:
    st.header("About this project")
    st.write(
        "Mini-project: CNN trained on the Intel Image Classification dataset "
        "(6 natural scene categories)."
    )
    st.write("**Classes:**")
    for c in CLASS_NAMES:
        st.write(f"- {c}")
    st.markdown("---")
    st.caption("Aditya Roshan S | 24BAI10227 | VIT Bhopal")


# ---------------------------------------------------------
# Main UI
# ---------------------------------------------------------
st.title("🏞️ Intel Image Classification")
st.write(
    "Upload a natural scene image (building, forest, glacier, mountain, sea, or street) "
    "and the CNN model will predict its category."
)

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image", use_column_width=True)

    with st.spinner("Loading model and running prediction..."):
        model = load_model()
        processed = preprocess_image(image)
        predictions = model.predict(processed)[0]

    predicted_index = int(np.argmax(predictions))
    predicted_class = CLASS_NAMES[predicted_index]
    confidence = float(predictions[predicted_index]) * 100

    st.success(f"Prediction: **{predicted_class.upper()}** ({confidence:.2f}% confidence)")

    st.subheader("Prediction probabilities")
    prob_dict = {CLASS_NAMES[i]: float(predictions[i]) for i in range(len(CLASS_NAMES))}
    st.bar_chart(prob_dict)

else:
    st.info("Please upload an image to get a prediction.")
