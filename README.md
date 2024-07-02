# hand-conrolled-media-player
Computer vision project create using python , mediapipe, hand gestures

This computer vision project built by using:

- mediapipe
- opencv

In this project one can control the media player such as YouTube or vlc by using hand gestures just by raising the fingers.

For example if you raise following fingers:

1 for forward
2 for backward
3 for volume up
4 for volume down
5 for pause or unpause the video

In First used opencv to read frames from webcam. Then detection of hand landmarks done using MediaPipe. And lastly a simple algorithm for detecting which fingers or how many fingers has been raised.
