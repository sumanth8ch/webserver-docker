from flask import Flask, request
from fractions import Fraction
from decimal import Decimal
app = Flask(__name__)
@app.route('/')
def index():
    return 'Usage;\nOperation?A=<Value1>&B=<Value2>\n'

@app.route('/add')
def addition():
    try:
        value1=request.args.get('A',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        value1='None'
    try:
        value2=request.args.get('B',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        value2='None'
    if value1 == 'None' or value2 == 'None' :
        return 'None'
    else:
        x = Fraction(value1)
        y= Fraction(value2)
        result= x+y
        return str(round(float(result),3))

@app.route('/sub')
def subtraction():
    try:
        value1=request.args.get('A',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        value1='None'
    try:
        value2=request.args.get('B',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        value2='None'
    if value1 == 'None' or value2 == 'None' :
        return 'None'
    else:
        x = Fraction(value1)
        y= Fraction(value2)
        result= x-y
        return(str(round(float(result),3)))


@app.route('/mul')
def multiplication():
    try:
        value1=request.args.get('A',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        value1='None'
    try:
        value2=request.args.get('B',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        value2='None'
    if value1 == 'None' or value2 == 'None' :
        return 'None'
    else:
        x = Fraction(value1)
        y= Fraction(value2)
        result= x*y
        return(str(round(float(result),3)))

@app.route('/div')
def division():
    try:
        value1=request.args.get('A',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        value1='None'
    try:
        value2=request.args.get('B',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        value2='None'
    if value1 == 'None' or value2 == 'None' :
        return 'None'
    else:
        x = Fraction(value1)
        y= Fraction(value2)
        try:
            result= x/y
            return(str(round(float(result),3)))
        except ZeroDivisionError as error:
            return 'None'

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=4080)
