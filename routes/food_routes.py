from flask import render_template, request, redirect, url_for

from app import app
from models import Session, Food
from data import food_data
from database import save_food_data, load_food_data


@app.route('/food', methods=['GET'])
def food_list():
    # foods = load_food_data()
    with Session() as session:
        foods = session.query(Food).all() #TODO що треба доставити після крапки?
    return render_template('food_list.html', foods=foods)


@app.route('/add/food', methods=['GET', 'POST'])
def add_foodd():
    if request.method == 'POST':
        # new_food = {
        #     "name": request.form['name'],
        #     "calories": request.form['calories'],
        #     "protein": request.form['protein'],
        #     "fat": request.form['fat'],
        #     "carbs": request.form['carbs'],
        #     "sugar": request.form['sugar']
        # }
        # food_data.append(new_food)
        # save_food_data(food_data)

        with Session() as session:
            food = Food(
                name=request.form['name'],
                calories=request.form['calories'],
                protein=request.form['protein'],
                fat=request.form['fat'],
                carbs=request.form['carbs'],
                sugar=request.form['sugar']
            )
            session.add(food)
            session.commit()
        return redirect(url_for('food_list'))
    return render_template('add_food.html')


@app.route('/delete/food/<int:food_id>', methods=['DELETE'])
def delete_food(food_id):
    # if 0 <= food_id < len(food_data):
    #     food_data.remove(food_id)
    #     save_food_data(food_data)

    with Session() as session:
        food = session.query(Food).filter(id == food_id).first()
        if food:
            session.delete(food)
            session.commit()
    return redirect(url_for('food_list'))


@app.route('/food/<int:food_id>/update', methods=['GET', 'PUT'])
def update_food(food_id):
    with Session() as session:
        food = session.query(Food).filter_by(id=food_id).first()
        if request.method == 'PUT':
            food.calories = request.form['calories']
            food.fat = request.form['fat']
            food.protein = request.form['protein']
            food.carbs = request.form['carbs']
            food.sugar = request.form['sugar']
            session.add(food)
            session.commit()
            return redirect(url_for('food_list'))
    return render_template('edit_food.html', food=food)
