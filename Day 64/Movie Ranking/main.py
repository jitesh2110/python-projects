from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from wtforms import StringField, SubmitField,IntegerField,FloatField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\PythonProject\Day 64\seafood.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] =mapped_column(String(500))
    year: Mapped[int] = mapped_column(Integer)
    description:Mapped[str] = mapped_column(String(500))
    rating: Mapped[float] = mapped_column(Float)
    ranking:Mapped[int] = mapped_column(Integer)
    review:Mapped[str] =mapped_column(String)
    img_url:Mapped[str]=mapped_column(String(1000))

with app.app_context():
    db.create_all()

class MovieForm(FlaskForm):
    title = StringField('movie name',validators=[DataRequired()])
    year = IntegerField('movie year',validators=[DataRequired()])
    description = StringField('movie dec', validators=[DataRequired()])
    rating =FloatField('movie rating', validators=[DataRequired()])
    ranking =IntegerField('movie ranking',validators=[DataRequired()])
    review = StringField('movie review',validators=[DataRequired()])
    img_url = StringField('movie img',validators=[DataRequired()])
    submit = SubmitField('Submit')

class RankingForm(FlaskForm):
    ranking = IntegerField('New Ranking', validators=[DataRequired()])
    submit = SubmitField('Update Ranking')

@app.route("/")
def home():
    all_movies = db.session.query(Movie).order_by(Movie.ranking).all()

    db.session.commit()
    movie_list = [{"id": movie.id, "title": movie.title, "description": movie.description, "rating": movie.rating,
                   "ranking":movie.ranking,"review":movie.review,"img_url":movie.img_url} for movie in all_movies]
    return render_template("index.html",movie = movie_list)

@app.route("/add",methods=["GET","POST"])
def add():
    form = MovieForm()
    if request.method == 'POST':
        title = request.form.get("title")
        year = request.form.get("year")
        description = request.form.get("description")
        rating = request.form.get("rating")
        ranking = request.form.get("ranking")
        review = request.form.get("review")
        img_url = request.form.get("img_url")

        data = Movie(
            title=title,
            year=int(year),
            description=description,
            rating=float(rating),
            ranking=int(ranking),
            review=review,
            img_url=img_url
        )
        db.session.add(data)
        db.session.commit()
        return render_template("add.html",form =form)


    return render_template("add.html",form = form)

@app.route("/update/<int:id>",methods=["GET","POST"])
def update(id):
    id = id
    rform = RankingForm()
    if request.method == 'POST':
        nranking = request.form.get("ranking")
        record = Movie.query.filter_by(id=id).first()
        record.ranking = int(nranking)
        db.session.commit()
        return render_template("edit.html", form=rform)

    return render_template("edit.html",form =rform)

@app.route("/delete/<int:id>",methods=["GET","POST"])
def delete(id):
    id =id
    record = Movie.query.get(id)
    if record:
        db.session.delete(record)
        db.session.commit()
        return redirect(url_for("home"))
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
