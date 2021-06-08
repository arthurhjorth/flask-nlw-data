from flask import Flask, request, jsonify, render_template
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def flask_nlw():
    model_name = request.args.get('model', '', type=str)
    print(f"serving {model_name}")
    if model_name != '':
        return render_template('data_collect.html', model_name=model_name)
    return jsonify({})


@app.route("/submit_data", methods=["POST", "GET"])
def submit_data():
    data = request.args.to_dict()
    print(data)
    return jsonify({})
