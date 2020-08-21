from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    nium_avatar = url_for('static', filename='img/nium-avatar.gif')
    marjorie_avatar = url_for('static', filename='img/marjorie-avatar.png')

    return render_template("main.html", nium_avatar=nium_avatar, marjorie_avatar=marjorie_avatar)

if __name__ == '__main__':
    app.run(debug=True)
