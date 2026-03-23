from flask import Blueprint, request, jsonify
from engine.orchestrator import process_lead
from models.lead_model import add_lead, get_all_leads
from models.workflow_model import get_logs

lead_bp = Blueprint("lead", __name__)

@lead_bp.route("/add-lead", methods=["POST"])
def add_new_lead():
    data = request.json

    if not data:
        return jsonify({"error": "No JSON received"}), 400

    required = ["name", "phone", "status", "interest_level"]

    for field in required:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    lead = {
        "name": data["name"],
        "phone": data["phone"],
        "status": data["status"],
        "interest_level": data["interest_level"]
    }

    add_lead(**lead)
    process_lead(lead)

    return jsonify({"message": "Lead processed successfully"})


@lead_bp.route("/leads", methods=["GET"])
def get_leads():
    return jsonify({"leads": get_all_leads()})


@lead_bp.route("/logs", methods=["GET"])
def logs():
    return jsonify({"logs": get_logs()})