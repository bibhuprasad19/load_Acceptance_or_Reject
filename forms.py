from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SubmitField
from wtforms.validators import DataRequired,Length

class MyForm(FlaskForm):
    gender=SelectField('Gender',choices=[(int(1),'Male'),(int(0),'Female')],validators=[DataRequired()])
    Married=SelectField('Married',choices=[(int(1),"Married"),(int(0),'Not Married')],validators=[DataRequired()])
    Dependents = SelectField('Dependents',choices=[(int(0),"0"),(int(1),'1'),(int(2),'2'),(int(3),'3+')],validators=[DataRequired()])
    Education = SelectField('Education',choices=[(int(1),"Not Graduate"),(int(0),'Graduate')], validators =[DataRequired(),Length(min=3,max=20)])
    Self_Employed = SelectField('Self_Employed',choices=[(int(1),"Yes"),(int(0),'NO')], validators=[DataRequired()])
    ApplicantIncome = IntegerField('ApplicantIncome', validators=[DataRequired(),Length(min=100,max=100000000)])
    CoapplicantIncome = IntegerField('Co-applicantIncome', validators=[DataRequired(),Length(min=0,max=1000000)])
    LoanAmount = IntegerField('Loan Amount', validators=[DataRequired(),Length(min=0,max=1000000)])
    LoanAmountTerm = IntegerField('LoanAmountTerm', validators=[DataRequired(), Length(min=6, max=48)])
    Property_Area = SelectField('Property_Area', choices=[(int(2), "URBAN"), (int(0), 'RURAL'), (int(1), 'SEMI-URBAN')], validators=[DataRequired()])
    Credit_History = SelectField('Credit_History', choices=[(int(1), "Yes"),(int(0), 'NO')], validators=[DataRequired()])
    submit=SubmitField('SUBMIT')