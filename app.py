from flask import Flask, render_template, request, redirect, url_for 
from data import food_data
from database import *
from models import Session, create_db
from database import load_food_data, save_food_data

app = Flask(__name__)

create_db()

@app.route('/food/list', methods=['GET'])
def food_list():
    foods = load_food_data()
    return render_template('food_list.html', foods=foods)

@app.route('/add/food', methods=['GET', 'POST'])
def add_foodd():
    if request.method == 'POST':
        new_food = {
            "name": request.form['name'],
            "calories": request.form['calories'],
            "protein": request.form['protein'],
            "fat": request.form['fat'],
            "carbs": request.form['carbs'],
            "sugar": request.form['sugar']
        }
        food_data.append(new_food)
        save_food_data(food_data)
        return redirect(url_for('food_list'))
    return render_template('add_food.html')

@app.route('/delete/food/<int:food_id>', methods=['POST'])
def delete_food(food_id):
    if 0 <= food_id < len(food_data):
        food_data.remove(food_id)
        save_food_data(food_data)
    return redirect(url_for('food_list'))



@app.route('/food/<int:food_id>/update', methods=['GET', 'POST'])
def update_food(food_id):
    with Session() as session:
        food = session.query(food).filter(food.id == food_id).first()
        if request.method == 'POST':
            food.calories = request.form['calories']
            food.fat = request.form['fat']
            food.protein = request.form['protein']
            food.carbs = request.form['carbs']
            food.sugar = request.form['sugar']
            session.commit()
            return redirect(url_for('food_list'))
    return render_template('edit_food.html', food=food)


@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True, port=5000)
