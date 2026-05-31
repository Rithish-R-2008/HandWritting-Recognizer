# Hand Recognition Application

A real-time hand recognition and gesture tracking application built with Python. This project leverages computer vision to detect hand landmarks, track movement, and recognize specific gestures through a standard webcam feed.

## 🚀 Features

*   **Real-Time Tracking:** High-speed hand landmark detection with minimal latency.
*   **Multi-Hand Support:** Detects and tracks multiple hands simultaneously.
*   **Gesture Recognition:** Identifies custom gestures (e.g., peace sign, thumbs up, fist).
*   **Visual Overlay:** Displays clear skeletal tracking lines and coordinate points on screen.

## 🛠️ Tech Stack

*   **Python 3.8+** - Core programming language.
*   **OpenCV** - Image processing and webcam video feed handling.
*   **MediaPipe** - Google's open-source framework for hand landmark detection.
*   **NumPy** - Mathematical operations for gesture calculation.

## 📦 Installation

Follow these steps to get your development environment running:

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd hand-recognition-app
   ```

2. **Create a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   *Note: Ensure your `requirements.txt` file contains at least `opencv-python`, `mediapipe`, and `numpy`.*

## 💻 Usage

To launch the application, run the main script from your terminal:

```bash
python main.py
```

*   Press **'q'** on your keyboard to exit the video stream feed safely.
*   Ensure your room is well-lit for optimal tracking accuracy.

## 🗺️ Hand Landmark Reference

This application maps 21 distinct hand landmark points based on the MediaPipe topology model (from Wrist [0] to Pinky Tip [20]). Custom gestures are calculated using the angles and distances between these specific nodes.

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn, inspire, and create. 

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
