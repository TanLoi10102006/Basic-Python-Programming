import sqlite3

# 1. Kết nối tới database (nếu chưa có thì sẽ tự tạo file mydata.db)
conn = sqlite3.connect("mydata.db")

# 2. Tạo đối tượng cursor để thực thi SQL
cursor = conn.cursor()

# 3. Tạo bảng (nếu chưa có)
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")

# 4. Thêm dữ liệu vào bảng
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Lợi", 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("An", 30))

# 5. Lưu thay đổi
conn.commit()

# 6. Đọc dữ liệu vừa thêm
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 7. Đóng kết nối
conn.close()
