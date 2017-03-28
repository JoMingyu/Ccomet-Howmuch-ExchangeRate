from database import Database
import crypt

db = Database()

@staticmethod
def encrypt(str):
    rows = db.execute("SELECT * FROM fernet_key")
    if not rows:
        # key가 없으면
        encrypted_str = crypt.crypt(str, 'keykey')
        return encrypted_str
        # db.execute("INSERT INTO fernet_key VALUES('", str(key), "')")
    else :
        key = rows[0]['key']
        print(key)

@staticmethod
def decrypt(str):
    rows = db.execute("SELECT * FROM fernet_key")
    if not rows:
        # key가 없으면
        # key = Fernet.generate_key()
        db.execute("INSERT INTO fernet_key VALUES('", key, "')")
    else :
        pass

print(encrypt('helloh'))