from flask import Blueprint, current_app, jsonify, request
from fvsapi.validate import validate
from fvsapi.service import services


fvs = Blueprint("fvs", __name__)


@fvs.route("/personal/verify/<pid>", methods=["POST"])
def prosonal_verify(pid):
    client_key = request.headers.get("API-KEY")

    config_key = current_app.config.get("KEY_SECRET")

    if client_key != config_key:
        return jsonify({"error": "Unauthorized"}), 401

    if not request.is_json:
        return jsonify({"valid": False, "error": "Invalid JSON"}), 400

    input_image = request.json.get("image")

    validate_pid = validate.is_valid_pid(pid)
    if not validate_pid:
        return jsonify({"valid": False, "error": "Invalid PID"}), 400

    validate_image = validate.is_base64(input_image)
    print(validate_image)
    if not validate_image[0]:
        return jsonify({"valid": False, "error": validate_image[1]}), 400

    return services.service_call_fvs_api(pid, input_image, config_key)
