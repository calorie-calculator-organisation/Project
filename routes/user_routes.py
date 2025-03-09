from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user', methods=['GET'])
def user_profile():
    return render_template('user_profile.html')


    