import sqlite3
conn = sqlite3.connect("sinhvien.db")
cu = conn.cursor()
cu.execute("""
CREATE TABLE IF NOT EXISTS sinhvien (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hoten TEXT NOT NULL,
    namsinh INTEGER,
    lop TEXT
)
""")
hoten=input("moi ban nhap ten ")
namsinh=int(input("moi ban nhap nam sinh"))
lop=int(input("moi ban nhap lop"))

cu.execute("INSERT INTO sinhvien (hoten, namsinh, lop) VALUES (?, ?, ?)", (hoten, namsinh, lop))

# 5. Lưu thay đổi
conn.commit()
cu.execute("SELECT * FROM sinhvien")
I =cu.fetchall()
for i in I :
    print(i)
conn.close()