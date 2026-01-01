import sqlite3
con = sqlite3.connect("AIassistant.db")
cursor = con.cursor()

# query = """
# CREATE TABLE IF NOT EXISTS sys_command (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL UNIQUE,
#     path TEXT NOT NULL
# )
# """
# cursor.execute(query)

# query = """
# CREATE TABLE IF NOT EXISTS web_command (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL UNIQUE,
#     url TEXT NOT NULL
# )
# """
# cursor.execute(query)
# # Delete all records
# cursor.execute("DELETE FROM sys_command;")
# cursor.execute("DELETE FROM web_command;")

# cursor.execute("DELETE FROM sys_command WHERE name=?",
#                ("chrome",))
# query = """
#      INSERT INTO sys_command VALUES(
#      null, 
#      'excel',
#      'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE'
#      )
# """
# cursor.execute(query)

# web_commands = (
#     ("linkedin", "https://www.linkedin.com//in//gauribelokar"),
    
# )

# cursor.executemany(
#     "INSERT OR IGNORE INTO web_command (name, url) VALUES (?, ?)",
#     web_commands
#     )

cursor.execute("DELETE FROM web_command WHERE name= ?",
               ("spotify",))

query = """
    INSERT INTO web_command VALUES(
    null, 
   'spotify',
   'https://open.spotify.com'
    )
"""
cursor.execute(query)


con.commit()
con.close()