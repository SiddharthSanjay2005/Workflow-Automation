from database import get_connection

def log_workflow(lead_name, action, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO workflow_logs (lead_name, action, status)
    VALUES (?, ?, ?)
    """, (lead_name, action, status))

    conn.commit()
    conn.close()

def get_logs():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM workflow_logs")
    logs = cursor.fetchall()
    conn.close()

    return logs