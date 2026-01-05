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
Before the simulation, make sure that you have import your robot stl file under ```/src/sim_desp/models/my_robot/meshes/``` and change the file name in ```/src/sim_desp/models/my_robot/model.sdf``` to fit your robot model file.
Then, recompile the workspace and run:
```bash
ros2 launch sim_gazebo sim_gazebo.launch.py 
```
