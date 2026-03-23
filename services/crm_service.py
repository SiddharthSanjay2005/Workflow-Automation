from utils.logger import log

def update_status(lead, new_status):
    old_status = lead["status"]
    lead["status"] = new_status
    log(f"CRM updated: {lead['name']} ({old_status} → {new_status})")