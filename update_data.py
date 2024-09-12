import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def update(conn, table, id, **kwargs):
    """
    Update columns in a table for a specific row id.
    :param conn: the Connection object
    :param table: table name
    :param id: row id
    :param kwargs: columns and their new values
    """
    try:
        # Check if the table exists
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table,))
        if not cur.fetchone():
            print(f"Table '{table}' does not exist.")
            return
        
        # Check if columns exist in the table
        cur.execute(f"PRAGMA table_info({table})")
        existing_columns = {row[1] for row in cur.fetchall()}
        invalid_columns = [col for col in kwargs if col not in existing_columns]
        if invalid_columns:
            print(f"Invalid columns: {', '.join(invalid_columns)}")
            return

        # Build and execute the update query
        parameters = [f"{k} = ?" for k in kwargs]
        parameters = ", ".join(parameters)
        values = tuple(v for v in kwargs.values())
        values += (id, )

        sql = f''' UPDATE {table}
                 SET {parameters}
                 WHERE id = ?'''
        cur.execute(sql, values)
        conn.commit()
        print("Update successful")
    except sqlite3.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    conn = create_connection("chess_training.db")
    if conn:
        update(conn, "training_sessions", 1, name="Advanced Tactics")
        conn.close()
