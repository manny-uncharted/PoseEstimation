This is a program that implements pose estimation using MediaPipe. It is based on the [MediaPipe Pose Estimation](https://google.github.io/mediapipe/solutions/pose) solution.

Here a simple base model is created in the poseEstimationMin.py file

And then it was scaled up to a much reusable module in poseModule.py.

The poseModule.py file is the main file that is used to run the program.

To make use of the code, you need to have the following libraries installed:
- OpenCV-python
- mediapipe

You can install them using the following command:
```bash
pip install opencv-python mediapipe
```
To run the program, you can use the following command:
```bash
python poseModule.py
```
Note: Ensure you have a video file named "video.mp4" in the same directory as the program. And you can change the video by changing the video in the cap variable in the poseModule.py file.