from flask import Flask, request, jsonify, render_template
app = Flask(__name__)


@app.route("/")
def flask_nlw():
    model_name = request.args.get('model', '', type=str)
    print(f"serving {model_name}")
    if model_name != '':
        return render_template('data_collect.html', model_name=model_name)
    return jsonify({})

