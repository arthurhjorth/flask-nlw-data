from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route("/model/<int:version>/<string:model_name>", methods=["POST", "GET"])
def model_version(version, model_name):
    print(f"serving {model_name}")
    if version == 1:
        return render_template('data_collectV1.html', model_name=model_name)
    ## this is for future versions of NetLogoWeb which may nneeneed another template
    return jsonify({})

@app.route("/submit_data", methods=["POST", "GET"])
def submit_data():
    print("received data")
    data = request.args.to_dict()
    print(data)
    return jsonify({})
