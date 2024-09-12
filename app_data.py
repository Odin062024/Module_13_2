import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def add_training_session(conn, session):
    """Add a new training session."""
    sql = '''INSERT INTO training_sessions(name, start_date, end_date)
             VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, session)
    conn.commit()
    return cur.lastrowid

def add_game(conn, game):
    """Add a new game to a training session."""
    sql = '''INSERT INTO games(training_session_id, opponent, result, date)
             VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, game)
    conn.commit()
    return cur.lastrowid

if __name__ == "__main__":
    conn = create_connection("chess_training.db")
    if conn:
        session = ("Opening Tactics", "2024-09-01", "2024-09-05")
        session_id = add_training_session(conn, session)
        
        game = (session_id, "Player A", "Win", "2024-09-02")
        add_game(conn, game)
        
        conn.close()
