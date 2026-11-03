from ultralytics import YOLO
import streamlit as st
from PIL import Image

@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    img = Image.open(picture)
    results = model.predict(img)
    
    
    annotated = results[0].plot()
    
    st.image(annotated, caption="Prediction", channels="BGR", width=400)