from cryptography.fernet import Fernet
from database import Database

db = Database()

def encrypt(str):
    rows = db.execute("SELECT * FROM fernet_key")
    if not rows:
        # key가 없으면
        key = Fernet.generate_key()
        f = Fernet(key)
        token = f.encrypt(b"adfasdfasd")
        print(token)
        # db.execute("INSERT INTO fernet_key VALUES('", str(key), "')")
    else :
        key = rows[0]['key']
        print(key)

def decrypt(str):
    rows = db.execute("SELECT * FROM fernet_key")
    if not rows:
        # key가 없으면
        key = Fernet.generate_key()
        db.execute("INSERT INTO fernet_key VALUES('", key, "')")
    else :
        pass