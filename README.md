# Eurobot-2026-Sim
This repository contains the simulation system using Gazebo for the Eurobot 2026 competition.
## Start with Docker
### Build image and container
```bash
cd docker/
docker compose up -d
```
### Build workspace
Attach to the running container:
```bash
docker exec -it sim-ws bash
```
Inside the container, build the workspace:
```bash
source /opt/ros/humble/setup.bash
colcon build
source install/setup.bash
```
### Run simulation
Before the simulation, please make sure that you have import your robot stl file under ```src/EurobotField_Sim/sim_desp/models/my_robot/meshes/``` and change the file name in ```src/EurobotField_Sim/sim_desp/models/my_robot/model.sdf``` to fit your robot model file.
Then, rebuild the workspace and run:
```bash
ros2 launch sim_gazebo sim_gazebo.launch.py 
```
If you don't see models in gazebo, please run the following command and launch the node again:
```bash
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/sim_ws/install/sim_desp/share/sim_desp/models
```
