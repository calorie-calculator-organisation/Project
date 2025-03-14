from flask import Flask, render_template
from models import Session, User
app = Flask(__name__)

@app.route('/user/<int:id>', methods=['GET'])
def user_profile(id):
    with Session() as session:
        user = session.query(User).filter_by(id=id).one()
    return render_template('user_profile.html', user=user)


    