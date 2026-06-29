from flask import Flask, request, jsonify
import json
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

OUTPUT_FILE = "/home/ec2-user/submissions.txt"
SAST = ZoneInfo("Africa/Johannesburg")

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()
        timestamp = datetime.now(SAST).strftime("%Y-%m-%d %H:%M:%S SAST")

        print("Webhook received!")

        with open(OUTPUT_FILE, "a") as f:
            f.write(f"\n{'='*60}\n")
            f.write(f"Time: {timestamp}\n")
            f.write(f"{'='*60}\n")
            f.write(json.dumps(data, indent=2))
            f.write("\n")

        return jsonify({"status": "success"}), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"status": "error"}), 500