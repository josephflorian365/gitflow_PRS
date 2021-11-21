from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Valle Grande!"

#Suma
@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int):
    nums_sum = a + b
    return f"La suma es: {str(nums_sum)}"

#Multiplicacion
# @app.route('/multiply/<int:a>/<int:b>')
# def sum(a: int, b: int):
#     nums_mul = a * b
#     return f"La suma es: {str(nums_mul)}"
