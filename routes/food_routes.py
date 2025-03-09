from flask import Flask, render_template, request, redirect, url_for
from data import food_data
from database import save_food_data, load_food_data

app = Flask(__name__)

@app.route('/food', methods=['GET'])
def food_list():
    foods = load_food_data()
    return render_template('food_list.html', foods=foods)

# @app.route('/add/food', methods=['GET', 'POST'])
# def add_food():
#     if request.method == 'POST':
#         new_food = {
#             "name": request.form['name'],
#             "calories": request.form['calories'],
#             "protein": request.form['protein'],
#             "fat": request.form['fat'],
#             "carbs": request.form['carbs'],
#             "sugar": request.form['sugar']
#         }
#         food_data.append(new_food)
#         save_food_data(food_data)
#         return redirect(url_for('food_list'))
#     return render_template('add_food.html')

