#Chat GPTにて作成
from flask import Flask, request, jsonify

app = Flask(__name__)

# IPアドレスデータベース（簡易的なデモ用）
ip_database = {
    "192.168.1.1": {"device": "Router", "status": "active"},
    "192.168.1.2": {"device": "Switch", "status": "inactive"}
}

@app.route("/ip", methods=["GET", "POST"])
def manage_ip():
    if request.method == "GET":
        return jsonify(ip_database)
    elif request.method == "POST":
        data = request.json
        ip = data.get("ip")
        info = data.get("info")
        if ip and info:
            ip_database[ip] = info
            return jsonify({"message": "IP added/updated", "data": ip_database})
        else:
            return jsonify({"error": "Invalid data"}), 400

if __name__ == "__main__":
    app.run(debug=True)
