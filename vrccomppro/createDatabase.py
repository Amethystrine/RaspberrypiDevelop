import sqlite3

# SQLiteデータベースに接続
conn = sqlite3.connect('member.sqlite')

# カーソルを取得
cursor = conn.cursor()

# テーブルを作成
cursor.execute('''CREATE TABLE IF NOT EXISTS mytable
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  registration_number TEXT,
                  registration_date TEXT,
                  name TEXT,
                  atcoder_id TEXT)''')

# データベースの変更を保存
conn.commit()

# 接続を閉じる
conn.close()
