from flask import Flask, make_response, jsonify
from flask_restful import Api
import logging


################# App initialization #################
app = Flask(__name__)
api = Api(app)


################# Logger initialization #################
format = "[%(asctime)s] %(levelname)s in %(name)s: %(message)s"
logging.basicConfig(level=logging.DEBUG, format=format)
logger = logging.getLogger("moniic")


################# Error handling #################
# Function to return each error with the same format
def make_error_response(error, code):
    response = {
        "status": "failed",
        "error_code": code,
        "error_message": f"Error. {str(error)}"
    }
    return make_response(jsonify(response), code)


@app.errorhandler(404)
def handle_error(error):
    return make_error_response(error, 404)


@app.errorhandler(TypeError)
def type_error_handler(error):
    return make_error_response(error, 415)


@app.errorhandler(ValueError)
@app.errorhandler(MemoryError)
@app.errorhandler(AttributeError)
def binascii_error_handler(error):
    return make_error_response(error, 500)