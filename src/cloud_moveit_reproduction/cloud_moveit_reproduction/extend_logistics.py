#!/usr/bin/env python3
import pandas as pd
import requests
import time
import numpy as np

# Synthetic Cornell-like dataset (based on real statistics: x~0.5±0.1, y~-0.1±0.2, z~0.03±0.01)
np.random.seed(42)  # Reproducible
df = pd.DataFrame({
    'x': np.random.normal(0.5, 0.1, 10),
    'y': np.random.normal(-0.1, 0.2, 10),
    'z': np.random.normal(0.03, 0.01, 10)
})

# Sample one grasp
sample = df.sample(1).iloc[0]

# Payload for logistics (warehouse pick: offset for box reach)
payload = {
    "start": [sample['x'], sample['y'], sample['z'], 0, 0, 0, 1],
    "goal": [sample['x'] + 0.15, sample['y'] + 0.1, sample['z'] + 0.05, 0, 0, 0, 1]
}

print(f"Logistics scenario: Warehouse grasping (Cornell-like synthetic)")
print(f"Start: ({sample['x']:.3f}, {sample['y']:.3f}, {sample['z']:.3f})")
print(f"Goal:  ({sample['x']+0.15:.3f}, {sample['y']+0.1:.3f}, {sample['z']+0.05:.3f})")

start = time.time()
try:
    resp = requests.post("http://127.0.0.1:5000/plan", json=payload, timeout=10)
    latency = time.time() - start
    if resp.status_code == 200:
        print(f"Logistics plan (cloud): {latency:.3f}s")
    else:
        print(f"Server error: {resp.status_code}")
except Exception as e:
    print(f"Cloud server not running: {e}")
