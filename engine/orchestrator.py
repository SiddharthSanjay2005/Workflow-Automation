from engine.rules_engine import evaluate_lead
from engine.retry_handler import retry_operation
from services.email_service import send_email
from services.sms_service import send_sms
from services.crm_service import update_status
from models.workflow_model import log_workflow
from utils.logger import log

def process_lead(lead):
    decision, score = evaluate_lead(lead)

    log(f"{lead['name']} → Score: {score}, Decision: {decision}")
    log_workflow(lead["name"], "Decision", decision)

    if decision == "HIGH_PRIORITY":
        retry_operation(send_email, lead["name"])
        log_workflow(lead["name"], "Email", "SUCCESS")

        retry_operation(send_sms, lead["phone"])
        log_workflow(lead["name"], "SMS", "SUCCESS")

        update_status(lead, "qualified")

    elif decision == "FOLLOWUP":
        retry_operation(send_email, lead["name"])
        log_workflow(lead["name"], "Followup Email", "SUCCESS")

        update_status(lead, "contacted")

    else:
        log_workflow(lead["name"], "No Action", "SKIPPED")