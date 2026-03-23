from config import RULES

def calculate_score(lead):
    score = lead["interest_level"] * 10

    if lead["status"] == "new":
        score += 20

    return score


def evaluate_lead(lead):
    score = calculate_score(lead)

    if score >= RULES["high_priority"]:
        return "HIGH_PRIORITY", score
    elif score >= RULES["followup"]:
        return "FOLLOWUP", score
    else:
        return "LOW_PRIORITY", score