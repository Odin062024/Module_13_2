import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def delete_where(conn, table, **kwargs):
    """
    Delete rows from table where attributes match the given conditions
    :param conn: Connection to the SQLite database
    :param table: table name
    :param kwargs: dict of attributes and values
    :return:
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

        # Build and execute the delete query
        qs = [f"{k} = ?" for k in kwargs]
        q = " AND ".join(qs)
        values = tuple(v for v in kwargs.values())

        sql = f"DELETE FROM {table} WHERE {q}"
        cur.execute(sql, values)
        conn.commit()
        print("Deleted")
    except sqlite3.Error as e:
        print(f"Error: {e}")

def delete_all(conn, table):
    """
    Delete all rows from table
    :param conn: Connection to the SQLite database
    :param table: table name
    :return:
    """
    try:
        # Check if the table exists
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table,))
        if not cur.fetchone():
            print(f"Table '{table}' does not exist.")
            return

        # Execute the delete query
        sql = f"DELETE FROM {table}"
        cur.execute(sql)
        conn.commit()
        print("Deleted")
    except sqlite3.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    conn = create_connection("chess_training
