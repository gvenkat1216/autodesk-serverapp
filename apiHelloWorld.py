from flask import Flask, request, jsonify, logging

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home_get():
    app.logger.info(request.url)
    app.logger.info(request.headers)
    if 'accept' in request.headers and 'application/json' in request.headers['accept']:
        return jsonify({"message": "Hello, World"})
    return "<p> Hello, World </p>"


@app.route('/', methods=['POST'])
def home_post():
    app.logger.info(request.url)
    app.logger.info(request.headers)
    return jsonify({"message": "POST"})


@app.errorhandler(404)
def page_not_found(e):
    app.logger.info(request.url)
    app.logger.info(request.headers)
    app.logger.error(e)
    return e


app.run()
