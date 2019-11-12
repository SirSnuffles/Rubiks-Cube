# Rubiks-Cube
Creates a visual representation of a cube and solves it in real life

ToRun;

install python3;

install pip (if not installed);

install libs using following commands;

pip install pyopengl

pip install pillow

pip install pygame

pip install webcolors

pip install opencv-python

run FullCube.py using python FullCube.py

1-9 and f1-f9 manual control, (missing middle movements as they dont line up with motor control, yet)

right click to add 10 random moves to queue

left click to add a solve algorithm to the queue

arrow keys to rotate the cube around axis

TODO@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Implement Solve algorithm (maybe left click to deterministically add a solve algorithm (can have solve instructions), left click twice to have an AI solve it)

Replace surfaces of cube with an image. (adding a .jpg to an opengl stack will cause issues) Conversion of some sort will be needed

Implement camera and reading pixel values of camera (mounting a camera may be an issue)

Implement reading of twitch chat (Twitch has a half second delay that may cause problems (may need to host a webserver, unsure...))

