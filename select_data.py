import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def select_all(conn, table):
    """
    Query all rows in the table
    :param conn: the Connection object
    :param table: the table name
    :return: list of rows or an empty list if error occurs
    """
    try:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table}")
        rows = cur.fetchall()
        return rows
    except sqlite3.Error as e:
        print(f"Error while retrieving data: {e}")
        return []

def select_where(conn, table, **query):
    """
    Query rows from table based on conditions in **query
    :param conn: the Connection object
    :param table: the table name
    :param query: dict of attributes and values
    :return: list of rows or an empty list if error occurs
    """
    try:
        cur = conn.cursor()
        qs = [f"{k} = ?" for k in query]
        q = " AND ".join(qs)
        values = tuple(v for v in query.values())
        sql = f"SELECT * FROM {table} WHERE {q}"
        cur.execute(sql, values)
        rows = cur.fetchall()
        return rows
    except sqlite3.Error as e:
        print(f"Error while retrieving data: {e}")
        return []

if __name__ == "__main__":
    conn = create_connection("chess_training.db")
    if conn:
        sessions = select_all(conn, "training_sessions")
        for session in sessions:
            print(session)
        
        games = select_where(conn, "games", opponent="Player A")
        for game in games:
            print(game)
        
        conn.close()
