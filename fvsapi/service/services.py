from flask import jsonify
import requests


def service_call_fvs_api(pid: int, image: str, key: str):
    try:
        url = f"https://events.controldata.co.th/mock-up/fvs/personal/verify/{pid}"
        headers = {
            "API-KEY": key,
            "Content-Type": "application/json",
        }
        body = {"image": image}
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(response.json()), response.status_code
