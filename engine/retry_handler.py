import time
from config import MAX_RETRIES
from utils.logger import log

def retry_operation(func, *args):
    for attempt in range(MAX_RETRIES):
        try:
            return func(*args)
        except Exception as e:
            log(f"Retry {attempt+1} failed: {e}")
            time.sleep(1)

    log("Operation failed after retries")