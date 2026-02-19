import mysql.connector
from werkzeug.security import generate_password_hash

# ================== CONFIG DATABASE ==================
def get_db_connection_elva():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_apotek_elva"   # sesuaikan dengan nama DB kamu
    )

# ================== TAMBAH USER ==================
def add_user(nama, username, password, role):

    hashed_password = generate_password_hash(password)

    conn = get_db_connection_elva()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users_elva 
        (nama_elva, username_elva, password_elva, role_elva)
        VALUES (%s, %s, %s, %s)
    """, (nama, username, hashed_password, role))

    conn.commit()
    cursor.close()
    conn.close()

    print(f"User {username} berhasil ditambahkan!")

# ================== JALANKAN ==================
if __name__ == "__main__":
    add_user(
        nama="Arya Samsul",
        username="arya",
        password="123",
        role="kasir"
    )
