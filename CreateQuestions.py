# Create Questions table
# 05/06/2020 - Lee Staff - Initial version

import sqlite3

conn = sqlite3.connect("quizzer.db")

cursor = conn.cursor()

# Create the table
#cursor.execute("""DROP TABLE questions""")
cursor.execute("""CREATE TABLE questions
                    (qu_quiz_ref int, qu_no int, qu_question text, qu_a text, qu_b text, qu_c text, qu_d text, qu_answer text)
                """)

conn.commit
conn.close