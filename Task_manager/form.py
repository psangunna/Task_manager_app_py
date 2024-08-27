from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, HiddenField,BooleanField, SelectField
from wtforms.validators import  DataRequired, Length


class tareaForm(FlaskForm):
    """form of ideas"""
    id_tarea = HiddenField()
    contenido = StringField("Content", validators=[DataRequired(), Length(min = 1 )])
    categoria  = StringField("Category", validators=[DataRequired(), Length(min = 1 )])
    fecha_limite  = StringField("Deadline", validators=[DataRequired(), Length(min = 10, max = 10 )])
    hecha = HiddenField()

    submit = SubmitField("Saved")
