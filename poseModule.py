import cv2
import mediapipe as mp
import time

# Creating a class to handle the pose detection
class poseDetector():

    def __init__(self, mode=False, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5):

        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        # Create our Model
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        """
        I need to write a test that ensure that the values entered as parameters are valid (e.g. mode is a boolean, upBody is a boolean, smooth is a boolean, detectionCon is a float between 0 and 1, trackCon is a float between 0 and 1)
        """
        # self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth, self.detectionCon, self.trackCon)
        self.pose = self.mpPose.Pose()

    # This function will find the pose
    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        # Draw the landmarks
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

        return img

    # This function will find the position of the specific landmarks(parts of the body)
    def findPosition(self, img, draw=True):
        lmList = [] # List of landmarks
        if self.results.pose_landmarks:    
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)
                lm.x*w # x position of the landmark (lm multiplied by the width of the image)
                lm.y*h # y position of the landmark (lm multiplied by the height of the image)
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return lmList



    

def main():
    cap = cv2.VideoCapture('pose-videos/6.mp4')
    pTime = 0
    detector = poseDetector()
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img)
        print(lmList)

        """To check for a specific landmark, we can use the following code:"""
        # if len(lmList) != 0:
        #     lmList = detector.findPosition(img, draw=False)
        #     print(lmList[14])
        #     cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.imshow("Image", img)

        cv2.waitKey(1)



if __name__ == "__main__":
    main()