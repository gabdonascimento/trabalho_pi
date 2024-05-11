import pymysql.cursors

# Connect to the database
connection = pymysql.connect(
    host="localhost",
    user="user",
    password="passwd",
    database="db",
    cursorclass=pymysql.cursors.DictCursor,
)
