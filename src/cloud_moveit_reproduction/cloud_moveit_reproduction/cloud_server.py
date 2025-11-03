from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/plan', methods=['POST'])
def plan():
    data = request.json
    time.sleep(0.3)  # Simulate cloud compute
    return jsonify({
        "success": True,
        "time": 0.3,
        "trajectory": [[data['start'][0], data['start'][1], 0.3, 0,0,0,1]]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
