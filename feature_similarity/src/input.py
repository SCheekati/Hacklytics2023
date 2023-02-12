from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired

class Form(FlaskForm):
    country = StringField('Country', validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired()])
    height = FloatField("Height", validators=[DataRequired()])
    weight = FloatField("Weight", validators=[DataRequired()])
    submit = SubmitField('Submit')