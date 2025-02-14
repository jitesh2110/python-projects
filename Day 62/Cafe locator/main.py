import csv
from flask import Flask, render_template
from flask_bootstrap import Bootstrap,render_form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
Bootstrap(app)


class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('LocationCafe', validators=[DataRequired()])
    copen = StringField('OpenCafe', validators=[DataRequired()])
    cclose = StringField('CloseCafe', validators=[DataRequired()])
    coffee = StringField('CoffeeCafe', validators=[DataRequired()])
    wifi = StringField('WifiCafe', validators=[DataRequired()])
    power = StringField('PowerCafe', validators=[DataRequired()])

    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        line = f"{form.name.data},{form.location.data},{form.copen.data},{form.cclose.data},{form.coffee.data},{form.wifi.data},{form.power.data}"
        with open("cafe-data.csv",mode='a',encoding='utf-8') as file:
            file.write(f"{line}\n")

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='',encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)

    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
