import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# CORRECTED Angle Calculation
def calculate_angle(a, b, c):
    a = np.array(a) # Shoulder
    b = np.array(b) # Elbow
    c = np.array(c) # Wrist
    
    # Calculate radians using Y and X coordinates specifically
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle > 180.0:
        angle = 360-angle
    return angle 

cap = cv2.VideoCapture(0)

l_counter = 0 
r_counter = 0
l_stage = None
r_stage = None

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break
        
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        try:
            landmarks = results.pose_landmarks.landmark
            
            # Left Hand
            l_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            l_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            l_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            
            # Right Hand
            r_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            r_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            r_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

            # Angles
            l_angle = calculate_angle(l_shoulder, l_elbow, l_wrist)
            r_angle = calculate_angle(r_shoulder, r_elbow, r_wrist)

            # SHOW ANGLES ON SCREEN (For Debugging)
            cv2.putText(image, str(int(l_angle)), tuple(np.multiply(l_elbow, [640, 480]).astype(int)), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

            # Logic - Adjusted thresholds to be more forgiving
            if l_angle > 150: l_stage = "down"
            if l_angle < 40 and l_stage == 'down':
                l_stage = "up"
                l_counter += 1

            if r_angle > 150: r_stage = "down"
            if r_angle < 40 and r_stage == 'down':
                r_stage = "up"
                r_counter += 1

        except: pass

        # UI Styling
        color = (0, 255, 0) if (l_stage == "up" or r_stage == "up") else (0, 0, 255)
        cv2.rectangle(image, (0,0), (250, 150), color, -1)
        cv2.putText(image, f'LEFT: {l_counter}', (10,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
        cv2.putText(image, f'RIGHT: {r_counter}', (10,80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
        cv2.putText(image, f'STAGE: {l_stage}', (10,120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)

        cv2.imshow('Gym Tracker Debug', image)
        if cv2.waitKey(10) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()