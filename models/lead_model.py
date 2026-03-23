from database import get_connection

def add_lead(name, phone, status, interest_level):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO leads (name, phone, status, interest_level)
    VALUES (?, ?, ?, ?)
    """, (name, phone, status, interest_level))

    conn.commit()
    conn.close()

def get_all_leads():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM leads")
    leads = cursor.fetchall()
    conn.close()

    return [
        {
            "id": l[0],
            "name": l[1],
            "phone": l[2],
            "status": l[3],
            "interest_level": l[4]
        }
        for l in leads
    ]