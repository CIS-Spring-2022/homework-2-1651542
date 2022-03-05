from flask import Flask, request, jsonify
from db import DB
from datetime import datetime

app = Flask(__name__)

@app.route("/api/animal", methods=["GET", "PUT", "POST", "DELETE"])
def animal():
    # Get animal by id
    if request.method == "GET":
        id = request.args["id"]
        data = DB.query("SELECT * FROM zoo WHERE id=%s", (id,))
        return jsonify(data[0]) if data else ""

    # Create new animal
    if request.method == "PUT":
        animal = request.args["animal"]
        gender = request.args["gender"]
        subtype = request.args["subtype"]
        age = request.args["age"]
        color = request.args["color"]

        ret = DB.query("INSERT INTO zoo VALUES(%s, %s, %s, %s, %s, %s)", (None, animal, gender, subtype, age, color))
        DB.query("INSERT INTO logs VALUES(%s, %s, %s, %s)", (None, datetime.now().strftime("%Y-%m-%d %H:%M"), ret, "Added animal"))
        return "", 200

    # Create new animal
    if request.method == "POST":
        animal = request.form["animal"]
        gender = request.form["gender"]
        subtype = request.form["subtype"]
        age = request.form["age"]
        color = request.form["color"]

        ret = DB.query("INSERT INTO zoo VALUES(%s, %s, %s, %s, %s, %s)", (None, animal, gender, subtype, age, color))
        DB.query("INSERT INTO logs VALUES(%s, %s, %s, %s)", (None, datetime.now().strftime("%Y-%m-%d %H:%M"), ret, "Added animal"))
        return "", 200

    # Delete animal by id
    if request.method == "DELETE":
        id = request.args["id"]

        DB.query("DELETE FROM zoo WHERE id=%s", (id,))
        DB.query("INSERT INTO logs VALUES(%s, %s, %s, %s)", (None, datetime.now().strftime("%Y-%m-%d %H:%M"), id, "Deleted animal"))
        return "", 200


@app.route("/api/logs", methods=["GET"])
def logs():
    # Check if reset parameter has been passed
    reset = request.args.get("reset", False)
    # If so, truncate logs table
    if reset:
        DB.query("TRUNCATE TABLE logs")
    # Return all logs
    return jsonify(DB.query("SELECT * FROM logs"))


app.run(debug=True)