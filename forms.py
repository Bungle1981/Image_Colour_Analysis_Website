from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, DecimalField, RadioField, FileField
from wtforms.validators import DataRequired, URL
from flask_wtf.file import FileRequired


class UploadForm(FlaskForm):
    file=FileField(validators=[FileRequired()])
    submit=SubmitField("Upload Image")