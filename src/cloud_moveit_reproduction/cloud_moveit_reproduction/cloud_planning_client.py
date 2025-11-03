#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import requests
import time

class CloudClient(Node):
    def __init__(self):
        super().__init__('cloud_client')
        self.get_logger().info('Starting cloud planning...')

    def run(self):
        payload = {
            "start": [0.4, -0.2, 0.4, 0, 0, 0, 1],
            "goal": [0.6, 0.3, 0.5, 0, 0, 0, 1]
        }
        start = time.time()
        try:
            resp = requests.post("http://127.0.0.1:5000/plan", json=payload, timeout=10)
            latency = time.time() - start
            self.get_logger().info(f"Cloud plan received in {latency:.3f}s")
        except Exception as e:
            self.get_logger().warn(f"Cloud failed: {e}")

def main():
    rclpy.init()
    node = CloudClient()
    node.run()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
