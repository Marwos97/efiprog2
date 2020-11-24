from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import IntegerField, StringField, BooleanField, TextAreaField, validators, Form, FloatField, DecimalField

class AddSkin(Form):
    name = StringField('Nombre Skin', [validators.DataRequired()])
    price = DecimalField('Precio', [validators.DataRequired()])
    float = DecimalField('Desgaste', [validators.DataRequired()])
    stock = IntegerField('Stock', [validators.DataRequired()])
    image = FileField('Imagen skin', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])