from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from calc_calorie import Calorie
from get_temperature import Temperature

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template("index.html")


class CaloriePage(MethodView):

    def get(self):
        calories_form = CalorieForm()

        return render_template("calories_web_form.html",
                               calorie_form=calories_form)

    def post(self):
        calories_form = CalorieForm(request.form)

        temperature = Temperature(country=calories_form.country.data,
                                  city=calories_form.city.data).get()

        calorie = Calorie(age=calories_form.age.data,
                          weight=calories_form.weight.data,
                          height=calories_form.height.data,
                          temperature=temperature)

        calories = calorie.calculate()

        return render_template("calories_web_form.html",
                               calorie_form=calories_form,
                               calories=calories,
                               result=True)


class CalorieForm(Form):
    weight = StringField("Weight: ", default=85)
    height = StringField("Height: ", default=184)
    age = StringField("Age: ", default=19)
    country = StringField("Country: ", default="USA")
    city = StringField("City: ", default="New York")
    button = SubmitField("Calculate")


app.add_url_rule("/",
                 view_func=HomePage.as_view("home_page"))
app.add_url_rule("/CaloriePage",
                 view_func=CaloriePage.as_view("calorie_page"))
app.run(debug=True)
