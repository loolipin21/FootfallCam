# FootfallCam: Staff Tag Detection via YOLOv8

The goal of this project is to build a **lightweight, fast, and reliable computer vision system** that detects the presence of **staff members wearing clips** in CCTV footage.

To achieve this, a **YOLOv8s model** was trained to detect the clips based on annotated video frames.

---

## 📁 Project Structure

```
.
├── frames/                      # Extracted video frames
├── runs/detect/clip-detector/  # YOLOv8 output folder
│   ├── weights/best.pt         # Trained model weights
│   └── predict.mp4             # Sample output video with predictions
├── model_train.ipynb           # Training notebook
└── clip.yaml                   # YOLO dataset configuration
```

---

## 🧠 Model Summary

- **Model Used**: [YOLOv8s](https://github.com/ultralytics/ultralytics)
- **Why YOLOv8s?**: Chosen for its balance between **speed** and **accuracy**
- **Framework**: PyTorch (Ultralytics YOLO)
- **Device**: Trained on CPU (GPU support available)

---

## 🧰 Steps Taken

### 1. 📹 Frame Extraction

Extracted **107 frames** from a source video at **2 FPS** using `ffmpeg`:

```bash
ffmpeg -i sample.mp4 -vf fps=2 frames/%05d.jpg
```

### 2. 🏷 Annotation

Annotated using **Label Studio**:
- **22 frames**: Contained **visible staff clips** (bounding boxes labeled)
- **85 frames**: Contained **no visible clips** (empty `.txt` label files used as negative examples)
- Clips were labeled tightly around the **visible area** of the tag, regardless of **blur** or **angle**

### 3. 🏋️ Model Training

Training settings:
- **Epochs**: 50  
- **Image Size**: 640x640  
- **Augmentations**:
  - Hue/Saturation/Value shifts
  - Horizontal flips
  - Rotation & scaling

Trained using:
```bash
yolo detect train data=clip.yaml model=yolov8s.pt epochs=50 imgsz=640
```

---

## 🎯 Results

- Processed **1341 frames** of surveillance video
- Despite training on only **22 positive samples**, the model **reliably detected** clips in new frames
- Performs well under **similar lighting** and **camera settings**
- Generalizes effectively for **same-camera deployments**

---

## 📦 Files

| File/Folder | Description |
|-------------|-------------|
| `frames/` | 107 annotated frames |
| `clip.yaml` | YOLO dataset configuration |
| `model_train.ipynb` | Training scripts |
| `best.pt` | Trained YOLOv8s weights |
| `predict.mp4` | Sample output video with predictions |

---

## 🚀 Future Work

- Add more diverse training data (lighting, angles, camera positions)
- Explore model pruning or quantization for embedded deployment
- Integrate with a real-time inference pipeline
