import pymysql
from config import RDS_HOST, RDS_PORT, RDS_USER, RDS_PASSWORD, RDS_DB_NAME

def get_connection():
    try:
        conn = pymysql.connect(
            host=RDS_HOST,
            port=RDS_PORT,
            user=RDS_USER,
            password=RDS_PASSWORD,
            db=RDS_DB_NAME
        )
        print("✅ RDS 연결 성공")
        return conn
    except Exception as e:
        print(f"❌ RDS 연결 실패: {e}")
        return None
