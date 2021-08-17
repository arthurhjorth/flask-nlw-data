import json, requests, copy
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

ur_data = json.load(open('secrets.json'))
url = "https://staging.quickstorage.scienceathome.org/save"


@app.route("/test/<string:model_name>", methods=["POST", "GET"])
def test(model_name):
    print(f"serving {model_name} on test")
    return render_template('test.html', model_name=model_name)

    ## this is for future versions of NetLogoWeb which may nneeneed another template
    return jsonify({})

@app.route("/model/<int:version>/<string:model_name>", methods=["POST", "GET"])
def model_version(version, model_name):
    print(f"serving {model_name}")
    if version == 1:
        return render_template('data_collectV1.html', model_name=model_name)
    if version == 2:
        return render_template('smithsonian.html', model_name=model_name)
    ## this is for future versions of NetLogoWeb which may nneeneed another template
    return jsonify({})

@app.route("/submit_smithsonian_data", methods=["POST", "GET"])
def submit_smithsonian_data():
    print("SMITHSONIAN")
    data = request.args.to_dict()
    print(data.values())
    return jsonify({})

@app.route("/submit_data", methods=["POST", "GET"])
def submit_data():
    print("received data")
    data = request.args.to_dict()
    data_dict = copy.deepcopy(ur_data)
    data_dict['data'] = json.loads(data['data'])
    print(data_dict)
    r = requests.post(url = url, json = data_dict)
    print(r)
    return jsonify({})
