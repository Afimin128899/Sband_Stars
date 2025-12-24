import sqlite3

conn = sqlite3.connect("data/db.sqlite3")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    stars REAL DEFAULT 0,
    total_withdraw REAL DEFAULT 0,
    refs INTEGER DEFAULT 0
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS withdraws (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    amount REAL,
    status TEXT DEFAULT 'pending',
    reason TEXT DEFAULT '',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)''')
conn.commit()

def add_user(user_id):
    cursor.execute("INSERT OR IGNORE INTO users(user_id) VALUES(?)", (user_id,))
    conn.commit()

def get_user(user_id):
    add_user(user_id)
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    return cursor.fetchone()

def add_stars(user_id, stars):
    add_user(user_id)
    cursor.execute("UPDATE users SET stars=stars+? WHERE user_id=?", (stars, user_id))
    conn.commit()

def add_ref(user_id):
    add_user(user_id)
    cursor.execute("UPDATE users SET refs=refs+1, stars=stars+2 WHERE user_id=?", (user_id,))
    conn.commit()

def add_withdraw(user_id, amount):
    cursor.execute("INSERT INTO withdraws(user_id, amount) VALUES(?,?)", (user_id, amount))
    conn.commit()

def set_withdraw_status(withdraw_id, status, reason=""):
    cursor.execute("UPDATE withdraws SET status=?, reason=? WHERE id=?", (status, reason, withdraw_id))
    conn.commit()

def get_withdraws(status=None):
    if status:
        cursor.execute("SELECT * FROM withdraws WHERE status=?", (status,))
    else:
        cursor.execute("SELECT * FROM withdraws")
    return cursor.fetchall()