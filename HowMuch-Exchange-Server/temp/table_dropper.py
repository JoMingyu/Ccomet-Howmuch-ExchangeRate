from database import database

db = database.Database()
db.execute("DELETE FROM account")
db.execute("DELETE FROM client_tokens")
db.execute("DELETE FROM current_exchange_rates")
db.execute("DELETE FROM daily_exchange_rate")
db.execute("DELETE FROM options")