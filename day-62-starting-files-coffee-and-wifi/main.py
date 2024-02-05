from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

coffee_emo = ['✘', '☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️']
wifi_emo = ['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪']
power_emo = ['✘', '🔌', '🔌🔌', '🔌🔌🔌️', '🔌🔌🔌🔌️']


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    open = StringField('Open', validators=[DataRequired()])
    close = StringField('Close', validators=[DataRequired()])
    coffee = SelectField('Coffee', choices=coffee_emo)
    wifi = SelectField('Wifi', choices=wifi_emo)
    power = SelectField('Power', choices=power_emo)
    submit = SubmitField('Submit')


# make all fields required except submit
# use a validator to check that the URL field has a URL entered.



css_url = "static/css/styles.css"


@app.route("/")
def index():
    return render_template("index.html", css_url=css_url)


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form, css_url=css_url)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows, css_url=css_url)


if __name__ == '__main__':
    app.run(debug=True)




