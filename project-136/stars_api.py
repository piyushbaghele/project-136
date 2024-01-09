# stars_api.py
from data1 import data
from flask import Flask, jsonify,request

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "data":data,
        "message":"Success"
    }),200

# Endpoint to display data of all the stars
@app.route('/stars')
def get_all_stars():
    planet_name = request.args.get('Star_name') 
    planet_data = next(item for item in data if item['Star_name']==planet_name)

    return jsonify({
        "data":planet_data,
        "message":"Success"
    }),200

if __name__ == '__main__':
    app.run(debug=True)
