# CS333-Final Project

### Kyle Knotek - Connect 4 Testing Workflow Pipeline - Docker Addition

### To use the testing pipeline:
Make a change in testscript.txt or any file and commit the change to the repository (any branch). Then go to actions and check if the pipeline fully processed. If sucessful, all of the steps should be completed and test script should have ran. You can check the program with test script output by clicking on the 'Main Program Test Script' step in the workflow. This test flow should create a docker image with the dockerfile in the directory.

### To run the created docker image in a container:
In the docker shell interface, use the command 'docker pull kknotek387/connect4_image:main'. Then, to create and run the container, use 'docker run -it kknotek387/connect4_image:main'. This runs the container in interactive mode and allows for playing of the game.
