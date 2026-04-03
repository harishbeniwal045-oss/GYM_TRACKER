# 🏋️‍♂️ AI Privacy-First Gym Tracker 

A real-time, computer vision-based fitness application that tracks bicep curls while prioritizing user privacy and form accuracy. Built with **Python**, **OpenCV**, and **MediaPipe**.

## 🌟 Key Features

* **Privacy Mode:** Automatically masks the user's face with a black "Privacy Circle" to ensure identity protection during workouts.
* **Posture Guard (Strict Mode):** Reps are only counted if the user maintains a straight posture. The system detects leaning by calculating the horizontal alignment between the shoulder and hip.
* **Dynamic UI Feedback:**
    * **Green Skeleton:** Correct form; ready to count.
    * **Red Skeleton:** Incorrect posture or out of frame; counting locked.
* **Live Angle Tracking:** Displays real-time joint angles ($0^\circ$ - $180^\circ$) directly on the elbow joints for instant feedback.
* **Dual-Arm Logic:** Independent counters for both Left and Right arm repetitions.

## 🛠️ Tech Stack

* **Language:** Python 3.9+
* **Computer Vision:** OpenCV
* **Pose Estimation:** MediaPipe (BlazePose)
* **Math:** NumPy (Trigonometric calculations)

## 📐 How It Works

The system uses the **Law of Cosines** to calculate the interior angle of the elbow joint. 



1.  **Detection:** MediaPipe identifies 33 3D landmarks on the body.
2.  **Privacy:** The "Nose" landmark is used as the center point to draw a black overlay over the face.
3.  **Validation:** The system checks if the absolute difference between `Shoulder_X` and `Hip_X` is within a strict threshold ($< 0.05$).
4.  **Counting:** A rep is registered only when the state changes from `DOWN` ($> 155^\circ$) to `UP` ($< 40^\circ$) while the posture is valid.

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/harishbeniwal045-oss/GYM_TRACKER.git](https://github.com/harishbeniwal045-oss/GYM_TRACKER.git)