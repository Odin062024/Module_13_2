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
        # Adding multiple training sessions
        sessions = [
            ("Opening Tactics", "2024-09-01", "2024-09-05"),
            ("Endgame Techniques", "2024-09-06", "2024-09-10"),
            ("Middle Game Strategies", "2024-09-11", "2024-09-15")
        ]
        
        session_ids = []
        for session in sessions:
            session_id = add_training_session(conn, session)
            session_ids.append(session_id)
        
        # Adding multiple games for each training session
        games = [
            (session_ids[0], "Koziołkiewicz", "Win", "2024-09-02"),
            (session_ids[0], "Matyjasek", "Draw", "2024-09-04"),
            (session_ids[1], "Aagard", "Loss", "2024-09-07"),
            (session_ids[1], "Karpow", "Win", "2024-09-09"),
            (session_ids[2], "Sacharewicz", "Draw", "2024-09-12"),
            (session_ids[2], "Nowak", "Win", "2024-09-14")
        ]
        
        for game in games:
            add_game(conn, game)
        
        conn.close()

