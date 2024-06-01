import sqlite3
import pandas as pd

def load_data():
    conn = sqlite3.connect('data/calls.db')
    query = "SELECT * FROM calls"
    data = pd.read_sql_query(query, conn)
    conn.close()
    return data
