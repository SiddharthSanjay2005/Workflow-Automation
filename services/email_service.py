import random
from utils.logger import log

def send_email(name):
    if random.choice([True, False]):
        log(f"Email sent to {name}")
    else:
        raise Exception("Email service failed")