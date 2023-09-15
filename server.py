from flask import Flask,jsonify,request


app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    content = request.get_json()
    firs = int(content['first'])
    second = int(content['second'])
    data={
        "result":firs+second
    }
    return jsonify(data),200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    content = request.get_json()
    first = int(content['first'])
    second = int(content['second'])
    data={
        "result":first-second
    }
    return jsonify(data),200

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
