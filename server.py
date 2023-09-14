from flask import Flask,jsonify


app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    content = request.get_json()
    first = content['first']
    second = content['second']
    data={
        result:first+second
    }
    return jsonify(data)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    content = request.get_json()
    first = content['first']
    second = content['second']
    data={
        result:first-second
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
