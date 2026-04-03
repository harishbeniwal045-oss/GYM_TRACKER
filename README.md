# 🏋️‍♂️ AI-Powered Personal Gym Tracker

An intelligent fitness application that uses **Computer Vision** to automate workout tracking. Built with **Python**, **OpenCV**, and **MediaPipe**, this tool accurately detects body posture and counts repetitions for bicep curls in real-time.

## 🌟 Features

* **Real-time Pose Estimation:** Utilizes MediaPipe's BlazePose model to track 33 body landmarks.
* **Dual-Arm Tracking:** Independent counters for both left and right arm repetitions.
* **Intelligent Angle Logic:** Uses trigonometric calculations to determine elbow joint angles, ensuring reps are only counted through a full range of motion.
* **Visual Debugging:** Displays live angle measurements on the screen to help users understand how their movement is being tracked.
* **Dynamic UI:** The status box changes color (Red/Green) based on the current movement stage (`up` or `down`).

## 🛠️ Tech Stack

* **Language:** Python 3.9+
* **Computer Vision:** OpenCV
* **Pose Estimation:** MediaPipe
* **Mathematics:** NumPy (Trigonometric calculations)

## 📐 How it Works

The system calculates the angle between the **Shoulder**, **Elbow**, and **Wrist** landmarks using the `arctan2` function to handle 2D coordinate geometry.

1.  **Stage "Down":** Triggered when the elbow angle exceeds **150°** (arm extended).
2.  **Stage "Up":** Triggered when the elbow angle drops below **40°** (arm curled).
3.  **Repetition:** A rep is only added to the counter when the arm successfully transitions from the "down" stage to the "up" stage.

## 🚀 Installation & Usage

1. Clone the repository:
   ```bash
   git clone [https://github.com/harishbeniwal045-oss/GYM_TRACKER.git](https://github.com/harishbeniwal045-oss/GYM_TRACKER.git)
