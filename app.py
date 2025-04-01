from flask import Flask, render_template, request

app = Flask(__name__)

# Función para calcular operaciones matemáticas
def calcular(num1, num2, operacion):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicacion":
        return num1 * num2
    elif operacion == "division":
        return num1 / num2 if num2 != 0 else "Error: División por cero"
    else:
        return "Operación no válida"

# Ruta principal con el formulario y el cálculo
@app.route('/', methods=['GET', 'POST'])
def home():
    resultado = None
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operacion = request.form['operacion']
        resultado = calcular(num1, num2, operacion)  # Llamamos la función directamente
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
