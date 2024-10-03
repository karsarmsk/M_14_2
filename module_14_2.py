import sqlite3
j=10
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
# for i in range(1,11):
#
#     cursor.execute(" INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#                    (f"user{i}", f"exampel{i}@gmail.com", f"{j}", "1000"))
#     j+=10

# for i in range(1,11,2):
#     cursor.execute(" UPDATE Users SET balance = ? WHERE username = ?",(500, f"user{i}"))

# for i in range(1,11,3):
#     cursor.execute(" DELETE FROM Users WHERE username = ?", (f"user{i}",))


# cursor.execute("SELECT username, email, age, balance, age FROM Users WHERE age != 60")
# users = cursor.fetchall()
# for user in users:
#     print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')
#

cursor.execute(" DELETE FROM Users WHERE id = ?", (6,)) # Удаление записи с id = 6
cursor.execute( "SELECT COUNT(*) FROM Users")  # общее количество записей
count_user = cursor.fetchone()[0]
# print(count_user)
cursor.execute( "SELECT SUM(balance) FROM Users") # сумма всех балансов
sum_balance = cursor.fetchone()[0]
# print(sum_balance)
cursor.execute( "SELECT AVG(balance) FROM Users") # средний баланс всех пользователей
avg_balance = cursor.fetchone()[0]
print(avg_balance)

connection.commit()
connection.close()