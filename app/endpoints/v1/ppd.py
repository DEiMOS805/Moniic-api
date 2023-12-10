from flask import request, make_response, jsonify
from flask_restful import Resource
import logging


logger = logging.getLogger("moniic.ppd_endpoint")


class PPD(Resource):
    def post(self):
        # Get the parameters from the request
        data = request.json
        logger.info(f"Data received: {data}")

        # Return the response
        response = {
            "status": "success",
            "message": "PPD endpoint",
            "args": data
        }
        return make_response(jsonify(response), 200)
