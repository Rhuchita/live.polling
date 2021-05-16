from flask import Flask, render_template, request, jsonify, flash, redirect
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__)

app.secret_key = "Polling_App"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Br!ght3n'
app.config['MYSQL_DB'] = 'polling'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM tbl ORDER BY id ASC")
    webframework = cur.fetchall()
    return render_template('index.html', webframework=webframework)


@app.route('/poll', methods=["POST", "GET"])
def polldata():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * from tblpoll"
    cur.execute(query)
    total_poll_r = int(cur.rowcount)
    cur.execute("SELECT * FROM tbl ORDER BY id ASC")
    framework = cur.fetchall()
    frameworkArr = []
    for row in framework:
        get_title = row['title']
        cur.execute(
            "SELECT * FROM tblpoll WHERE web_framework = %s", [get_title])
        row_poll = cur.fetchone()
        total_row = cur.rowcount

        percentage_vote = round((total_row/total_poll_r)*100)
        print(percentage_vote)
        if percentage_vote >= 75:
            progress_bar_class = 'progress-bar-success'
        elif percentage_vote >= 50 and percentage_vote < 75:
            progress_bar_class = 'progress-bar-info'
        elif percentage_vote >= 35 and percentage_vote < 50:
            progress_bar_class = 'progress-bar-warning'
        else:
            progress_bar_class = 'progress-bar-danger'

        frameworkObj = {
            'id': row['id'],
            'name': row['title'],
            'percentage_vote': percentage_vote,
            'progress_bar_class': progress_bar_class
        }
        frameworkArr.append(frameworkObj)
    return jsonify({'htmlresponse': render_template('response.html', frameworklist=frameworkArr)})


@app.route("/insert", methods=["POST", "GET"])
def insert():
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        poll_opt = request.form['poll_opt']
        print(poll_opt)
        cursor.execute(
            "INSERT INTO tblpoll (web_framework) VALUES (%s)", [poll_opt])
        mysql.connection.commit()
        cur.close()
        msg = "success"
    return jsonify(msg)


if __name__ == "__main__":
    app.run(debug=True)
