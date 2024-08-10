from flask import Flask, request, jsonify, render_template, make_response
from DB import DB
from glv_var import g_var
from DbObject import DbObject

app = Flask(__name__)
env = g_var.read_env(g_var.env_file)

db = DB(env["db_url"])
db.set_db(env["db_name"])
db.set_collection(env["db_col"])



@app.route("/api", methods=["POST"])
def api():
    data = request.get_json()
    return jsonify(data)
@app.route("/")
@app.route("/go/<alias>")
def home(alias:str = None):
    return render_template("index.html")


@app.route("/api/new", methods=["POST"])
@app.route("/new" ,methods=["POST"])
def new_url():
    data = request.get_json()
    if not data["url"]  or not data["alias"]:
        return jsonify({"error", "url or alias missing"}), 400

    obj = DbObject(g_var.url_schema).add(("url",data["url"])).add(("short_alias",data["alias"]))
    db.insert(obj)

    return jsonify({"success":{"_id":obj._id}}), 200

@app.route("/api/get/<alias>")
@app.route("/get/<alias>")
def get_url(alias:str):
    return jsonify(db.get_object({"short_alias":alias}).compile()), 200

@app.route("/get/<int:limit>")
def get_till(limit:int):
    obj_list = db.get_objects({},limit)
    return jsonify({"data":[obj.compile() for obj in obj_list]}), 200

@app.route("/api/edit/<alias>", methods=["POST"])
@app.route("/edit/<alias>", methods=["POST"])
def edit_url(alias:str):
    data = request.get_json()
    if not data["url"]:
        return jsonify({"error", "url missing"}), 400

    obj = db.get_object({"short_alias":alias})
    obj.update(("url",data["url"]))
    db.delete({"short_alias":alias})
    db.insert(obj)

    return jsonify({"success":{"_id":obj._id}}), 200
@app.route("/api/get")
@app.route("/get")
def get_all():
    obj_list = db.get_objects({})
    return jsonify({"data":[obj.compile() for obj in obj_list]}), 200

@app.route("/api/delete/<alias>")
@app.route("/delete/<alias>")
def delete_url(alias: str):
    # Perform the deletion from the database
    result = db.delete({"short_alias": alias})

    if result.deleted_count == 1:
        # Successfully deleted
        return make_response(jsonify({"message": "URL deleted successfully"}), 200)
    else:
        # URL not found
        return make_response(jsonify({"error": "URL not found"}), 404)

if __name__ == "__main__":
    app.run(debug=True)
