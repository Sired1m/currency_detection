# Bahrain Currency Detector

A Streamlit web app that detects Bahraini banknotes from a camera photo using a custom-trained YOLO model.

## Features
- Take a picture with your webcam or phone camera
- Detects the banknote and draws bounding boxes with labels and confidence scores

  ## Model
- Framework: [Ultralytics YOLO](https://docs.ultralytics.com/)
- Dataset: Bahrain currency images (exported in Ultralytics NDJSON format)
- Training code: see `model_training.ipynb`

## Notes
- Allow camera access in your browser when prompted.
- Use the same Ultralytics version you trained with, so `best.pt` loads correctly.
