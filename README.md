# Cloud-Enhanced MoveIt Motion Planning  
**Reproduction + Logistics Extension**  
*2023 Elsevier Paper: [DOI:10.1016/j.rcim.2023.102580](https://doi.org/10.1016/j.rcim.2023.102580)*

---

## Overview  
Reproduces cloud-offloaded motion planning using **ROS 2 + MoveIt 2** and extends it to **warehouse logistics** using synthetic grasping data.

**Key Result**: **36–39% latency reduction** via cloud offloading.

---

## Setup (Ubuntu 22.04)

```bash
# 1. Install ROS 2 Humble
sudo apt update && sudo apt install -y ros-humble-desktop-full

# 2. Create workspace
mkdir -p ~/moveit_cloud_ws/src
cd ~/moveit_cloud_ws

# 3. Clone MoveIt 2 Tutorials + Dependencies
cd src
git clone https://github.com/ros-planning/moveit2_tutorials.git -b humble
cd ..
vcs import src < moveit2_tutorials/moveit2_tutorials.repos

# 4. Install Python deps
pip3 install -r requirements.txt

# 5. Build
colcon build --symlink-install --parallel-workers 2
source install/setup.bash
