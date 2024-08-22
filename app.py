from flask import Flask, render_template, jsonify
import sqlite3
import json

app = Flask(__name__)

# データベースパス
db_path = './salary.db'
@app.route('/')
def index():
    # SQLiteデータベースに接続
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # データを取得するクエリ
    query = "SELECT player, season17_18 FROM NBA_season1718_salary ORDER BY season17_18 DESC LIMIT 50;"
    cursor.execute(query)
    rows = cursor.fetchall()
    
    # データを辞書に変換
    data = [{"player": row[0], "season17_18": row[1]} for row in rows]
    
    connection.close()
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)