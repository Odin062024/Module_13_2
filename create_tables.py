import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_tables(conn):
    """Create tables for the chess training database."""
    create_training_sessions_sql = """
    CREATE TABLE IF NOT EXISTS training_sessions (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT NOT NULL
    );
    """

    create_games_sql = """
    CREATE TABLE IF NOT EXISTS games (
        id INTEGER PRIMARY KEY,
        training_session_id INTEGER NOT NULL,
        opponent TEXT NOT NULL,
        result TEXT NOT NULL,
        date TEXT NOT NULL,
        FOREIGN KEY (training_session_id) REFERENCES training_sessions (id)
    );
    """
    
    try:
        cur = conn.cursor()
        cur.execute(create_training_sessions_sql)
        cur.execute(create_games_sql)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

if __name__ == "__main__":
    conn = create_connection("chess_training.db")
    if conn:
        create_tables(conn)
        conn.close()
