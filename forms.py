from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterForm(FlaskForm):
    email = StringField(label='Email',validators=[DataRequired(),
        validators.Length(min=8, message=(u'Little short for an email address?')),
        validators.Email(message=(u'Invalid email address.'))
    ])
    password = PasswordField(label='Password',validators=[DataRequired(),
    validators.Length(min=8, message=(u'Password must be atleast 8 characters long'))])
    name= StringField(label='Name', validators=[DataRequired()])
    submit= SubmitField(label='Sign Me Up!',validators=[DataRequired()])

class LoginForm(FlaskForm):
    email = StringField(label='Email',validators=[DataRequired(),
        validators.Length(min=8, message=(u'Little short for an email address?')),
        validators.Email(message=(u'Invalid email address.'))
    ])
    password = PasswordField(label='Password',validators=[DataRequired(),
    validators.Length(min=8, message=(u'Password must be atleast 8 characters long'))])
    submit= SubmitField(label='Let Me In!',validators=[DataRequired()])

class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")