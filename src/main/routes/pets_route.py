from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.errors.error_handler import handle_error

from src.main.composer.pet_lister_composer import pet_lister_composer
from src.main.composer.pet_deleter_composer import pet_deleter_composer

pet_route_bp = Blueprint('pets_routes', __name__)

@pet_route_bp.route("/pets", methods=["GET"])
def list_pets():
    try:
        http_request = HttpRequest(body=request.json)
        view = pet_lister_composer()

        http_response = view.handle_request(http_request)

        return jsonify(http_response.body), http_response.status_code 
    
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code


@pet_route_bp.route("/pets/<name>", methods=["DELETE"])
def pet_deleter(name):
    try:
        http_request = HttpRequest(param={"name": name})
        view = pet_deleter_composer()

        http_response = view.handle_request(http_request)

        return jsonify(http_response.body), http_response.status_code
    
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code