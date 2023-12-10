from flask import make_response, jsonify

from app.endpoints.v1.ppd import PPD
from app.endpoints.v1.pue import PUE
from app import app, api


################# path SETUP resources #################
api.add_resource(PPD, "/moniic/v1/ppd")
api.add_resource(PUE, "/moniic/v1/pue")

@app.route("/")
def index():
    response = {
        "status": "success",
        "message": "Bienvenido a la API que Capybara's Team ha creado para el proyecto de Moniic"
    }
    return make_response(jsonify(response), 200)


@app.after_request
def apply_caching(response):
    app.logger.info(app.logger)
    return response


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
