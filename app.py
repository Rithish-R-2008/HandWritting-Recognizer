import os
# Block TensorFlow's warning/info logs (0 = all logs, 1 = filter INFO, 2 = filter WARNING, 3 = filter ERROR)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import streamlit as st
import numpy as np
import cv2
import tensorflow as tf
from PIL import Image

import streamlit as st
import numpy as np
import cv2
import tensorflow as tf
from PIL import Image

# 1. Load the saved model and cache it so it doesn't reload on every click
@st.cache_resource
def load_my_model():
    # Make sure "handwritten_model.h5" is in the same directory as this script
    return tf.keras.models.load_model("handwritten_model.h5")

model = load_my_model()

# 2. UI Layout
st.title("✏️ Handwritten Character Recognition")
st.write("Upload an image of a single handwritten digit (0-9) to see the neural network predict it live.")

uploaded_file = st.file_uploader("Choose a digit image file...", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    # 3. Read the image file and convert it to grayscale
    image = Image.open(uploaded_file).convert('L')
    
    # CRITICAL FIX: Cast to uint8 explicitly to prevent OpenCV errors
    img_array = np.array(image, dtype=np.uint8)  
    
    # Display the uploaded image to the user
    st.image(img_array, caption='Uploaded Image', width=180)
    
    # 4. Preprocess the image to match MNIST standards (28x28 pixels)
    processed_img = cv2.resize(img_array, (28, 28))
    
    # SMART FIX: Invert colors if the user uploaded a dark digit on light paper.
    # MNIST models expect a white digit on a black background.
    if np.mean(processed_img) > 127:
        processed_img = cv2.bitwise_not(processed_img)
        
    # Normalize pixel values to [0, 1]
    processed_img = processed_img / 255.0
    
    # Reshape to match the model's expected input shape: (batch_size, height, width, channels)
    processed_img = processed_img.reshape(1, 28, 28, 1)
    
    # 5. Run the model prediction
    with st.spinner("Analyzing handwriting features..."):
        prediction = model.predict(processed_img)
        predicted_class = np.argmax(prediction)
        confidence = np.max(prediction) * 100
        
    # 6. Output the result
    st.success(f"### Predicted Digit: {predicted_class}")
    st.info(f"Model Confidence: {confidence:.2f}%")