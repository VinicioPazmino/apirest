from flask import Flask, jsonify, request
import jwt

app = Flask(__name__)

@app.route('/')
def hello():
	return "Pantalla de Inicio! Autor: Vinicio Pazmino"

@app.route('/DevOps', methods=['GET'])
def DevOpsGET():
    return 'ERROR'

@app.route('/DevOps', methods=['POST'])
def DevOpsPOST():
    print(request.json)
    encoded_jwt = jwt.encode( request.json, "firma", algorithm="HS256", headers={"kid": "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"},)
    return jsonify({"message" : "Hello Juan Perez your message will be send"},{"token":encoded_jwt})

@app.route('/DevOps', methods=['PUT'])
def DevOpsPUT():
    return 'ERROR'

@app.route('/DevOps', methods=['PATCH'])
def DevOpsPATCH():
    return 'ERROR'

@app.route('/DevOps', methods=['DELETE'])
def DevOpsDELETE():
    return 'ERROR'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)