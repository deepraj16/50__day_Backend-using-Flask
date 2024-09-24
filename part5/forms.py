from flask_wtf import FlaskForm
from wtforms import  (     StringField , SelectField  ,DateField ,PasswordField ,SubmitField ,BooleanField)

from wtforms.validators import (
    DataRequired ,# to validators the data is presnt 
    Length, # to give the len
    Email ,# to
    Optional,
    EqualTo, # to check the value to string are equal or not
    
)


class SignupFrom(FlaskForm):
    # filed
    # username
    # email
    # gender
    # DOB
    # password

    username =StringField(
         "Username",
        validators = [DataRequired(),Length(2,30)]

    )
    
    email = StringField(
        "email",
        validators=[DataRequired(),Email()],
    )

    gender =   SelectField(
        "Gender",
        choices=['Male',"Female","Other"],
        validate_choice=[Optional()]
    )
    dob =DateField(
        "Date of Birth" , 
        validators=[Optional()]
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(),Length(5,25)]
    )
    confirm_password = PasswordField(
        "Confirm Password" ,
        validators=[DataRequired(),Length(5,25),EqualTo('password')]
    )
    submit =SubmitField(
       "Sign up"
    )

class LoginFrom(FlaskForm):
    # Email
    # password
    # rember met
    email = StringField(
        "email",
        validators=[DataRequired(),Email()]
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(),Length(5,25)]
    )
    remeber_me = BooleanField(
        "Remember ME"
    )
    submit =SubmitField(
       "Login"
    )


