from db_connect import get_connection

def main():
    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT NOW();")
            result = cursor.fetchone()
            print(f"현재 시간: {result[0]}")
        conn.close()

if __name__ == "__main__":
    main()
