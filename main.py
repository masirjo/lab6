from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/",methods=['GET'])
def root():
    return "<h1>Ответ на запрос GET</h1>"

@app.route("/user",methods=['GET'])
def user():
    name = "Алина"
    marks = [5,4,3,4,5,5]
    return render_template('user.html',name = name,marks = marks)

if __name__ == "__main__":
    app.run()