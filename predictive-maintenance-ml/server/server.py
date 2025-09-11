from flask import Flask, jsonify, request
import util

app = Flask(__name__)

@app.route('/get_failure', methods=['GET','POST'])
def get_failure():
    type = request.form['type']
    air_T = float(request.form['air_T'])
    process_T =float(request.form['process_T'])
    rotational_speed = float(request.form['rotational_speed'])
    torque = float(request.form['torque'])
    tool_wear = float(request.form['tool_wear'])
    result = util.get_estimated_failure(type, air_T, process_T, rotational_speed, torque, tool_wear)
    response = jsonify({ 'estimated_failure': int(result)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
if __name__ == '__main__':
    print("Starting Python Flask server for failure prediction...")
    util.load_saved_artifacts()
    app.run() 