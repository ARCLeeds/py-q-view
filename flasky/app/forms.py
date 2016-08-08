from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Regexp
class PathForm(Form):
    path = StringField('Path', validators=[Required()])
    submit = SubmitField('submit')
