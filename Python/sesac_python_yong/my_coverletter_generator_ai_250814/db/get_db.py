from db.get_connection import get_connection

def get_all_sessions():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            sql = "SELECT session_id FROM session ORDER BY session_id"
            cur.execute(sql)
            rows = cur.fetchall()
            return [row['session_id'] for row in rows]
    finally:
        conn.close()
        
def get_all_corp_names():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            sql = "SELECT corp_name FROM corp_name ORDER BY corp_name_id"
            cur.execute(sql)
            rows = cur.fetchall()
            return [row['corp_name'] for row in rows]
    finally:
        conn.close()
        
def get_all_corp_ids():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            sql = "SELECT corp_name_id FROM corp_name ORDER BY corp_name_id"
            cur.execute(sql)
            rows = cur.fetchall()
            return [row['corp_name_id'] for row in rows]
    finally:
        conn.close()
