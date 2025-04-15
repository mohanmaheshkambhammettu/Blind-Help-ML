
# SmartVisionML

A mobile-based obstacle detection system to assist visually impaired individuals by identifying obstacles using a smartphone camera and providing real-time audio feedback.

---

## 📁 Project Structure

```
SmartVisionML/
├── data/               # Store your training images and annotations
├── models/             # Trained models and converted .tflite models
├── notebooks/          # Jupyter notebooks for training and experiments
├── src/                # Source code for model, utilities, etc.
│   ├── detector.py
│   └── utils/
│       └── helpers.py
├── android_app/        # Android integration logic
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
```

---

## ✅ Setup Instructions

### 1. Set Up Environment

```bash
cd SmartVisionML
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

### 2. Prepare Dataset

- Download a dataset like [MS COCO](https://cocodataset.org/) or [Open Images](https://storage.googleapis.com/openimages/web/index.html).
- Or collect your own obstacle images/videos using a smartphone.
- Place them in the `/data` folder.

---

### 3. Implement the Model

Edit `src/detector.py`:
```python
import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5n')  # Lightweight for mobile
results = model('data/sample.jpg')
results.print()
results.show()
```

---

### 4. Train the Model

Use `notebooks/train_model.ipynb` to:
- Load and preprocess the dataset
- Train the model
- Save it to `models/`

---

### 5. Convert Model for Mobile

```python
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model('models/my_model')
tflite_model = converter.convert()

with open('models/model.tflite', 'wb') as f:
    f.write(tflite_model)
```

---

### 6. Android Integration

In `android_app/main.py`, use Kivy or Chaquopy to integrate your `.tflite` model into an Android app.

Example (Chaquopy with Java):
```java
Interpreter tflite = new Interpreter(loadModelFile("model.tflite"));
```

---

### 7. Add Audio Feedback

```python
import pyttsx3

engine = pyttsx3.init()
engine.say("Obstacle ahead")
engine.runAndWait()
```

Or use Android's `TextToSpeech` for native apps.

---

### 8. Test and Optimize

- Stream camera feed and detect objects
- Provide real-time spoken alerts
- Quantize model for mobile optimization (int8)

---

## 🚀 Bonus Features

- Depth estimation for better obstacle distance
- Vibration alerts on close proximity
- GPS + navigation assistance
