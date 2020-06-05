# Create Quizzer db and Quiz table
# 05/06/2020 - Lee Staff - Initial version

import sqlite3

conn = sqlite3.connect("quizzer.db")

cursor = conn.cursor()

# Create the table
#cursor.execute("""DROP TABLE quiz""")
cursor.execute("""CREATE TABLE quiz
                    (qz_ref int, qz_title text, qz_by text, qz_questions int)
                """)

conn.commit
conn.close