## 1. System Setup  
- **OS**: Ubuntu 22.04 LTS  
- **ROS 2**: Humble Hawksbill  
- **MoveIt 2**: Built from source with 8 GB swap to avoid OOM

## 2. Architecture
Robot (ROS 2) → HTTP POST → Cloud Server (Flask) → Trajectory → Robot

## 3. Cloud Server  
- Simulates powerful remote node  
- 300ms artificial delay  
- Returns valid joint trajectory

## 4. Client  
- Sends start/goal poses  
- Measures round-trip latency

## 5. Logistics Extension  
- Synthetic data based on **Cornell Grasping Dataset**  
- Mean: `(x=0.5, y=-0.1, z=0.03)`  
- Std: `(0.1, 0.2, 0.01)`  
- Goal: offset by `(0.15, 0.1, 0.05)` → warehouse reach

## 6. Evaluation  
- Local: Full MoveIt pipeline  
- Cloud: Offloaded planning  
- Logistics: Domain transfer
