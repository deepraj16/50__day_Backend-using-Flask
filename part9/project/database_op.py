import sqlite3
import pandas as pd

# File and database paths
FILE_PATH = "vnn.csv"  # Path to your CSV file
DATABASE = "data.db"  # SQLite database file

# Load CSV into a pandas DataFrame
df = pd.read_csv(FILE_PATH)

# Connect to SQLite database
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

def __itin__():
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Vulnerabilities TEXT,
            links TEXT
        )
    ''')

    # Insert data from DataFrame into the database
    for _, row in df.iterrows():
        cursor.execute('''
            INSERT INTO records (Vulnerabilities, links)
            VALUES (?, ?)
        ''', (row['Vulnerabilities'], row['links']))
    conn.commit()
    conn.close()

def Select():
    cursor.execute('''
            select * from records
                ''')
    rows = cursor.fetchall() 
    return rows

def delete():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

def insert():
    print("Enter the vanabulity")
    vnn=input()
    print("Enter the links")
    links=input()
    cursor.execute(
        '''
        insert into records(Vulnerabilities,links) values(?,?)
        ''',(vnn,links)
    )
    conn.commit()
    conn.close()    

# Delete specific rows where a condition is met
def delete():
    cursor.execute('''
        DELETE FROM records WHERE Vulnerabilities = ?
    ''', (' CVE-2024-26859 ',))
    print("Data has been successfully delete from the database.")
    conn.commit()
    conn.close()


a=Select()
print(len(a))
print(a[0])
print("Name of Delete a Vulnerabilities")
# vun=input()
# delete()
# print("Data has been successfully inserted into the database.")
insert()



