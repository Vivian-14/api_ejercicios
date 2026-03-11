from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Página principal
@app.route('/')
def inicio():
    return render_template('index.html')

# API promedio
@app.route('/promedio', methods=['POST'])
def calcular_promedio():
    datos = request.get_json()

    nombre = datos['nombre']
    calificaciones = datos['calificaciones']

    promedio = sum(calificaciones) / len(calificaciones)

    respuesta = {
        "nombre": nombre,
        "promedio": promedio
    }

    return jsonify(respuesta)

# API convertir temperatura
@app.route('/convertir-temperatura', methods=['POST'])
def convertir_temperatura():
    datos = request.get_json()

    valor = datos['valor']
    escala = datos['escala']

    if escala.lower() == "celsius":
        resultado = (valor * 9/5) + 32
        destino = "Fahrenheit"

    elif escala.lower() == "fahrenheit":
        resultado = (valor - 32) * 5/9
        destino = "Celsius"

    else:
        return jsonify({"error": "Escala no válida"}), 400

    respuesta = {
        "resultado": resultado,
        "escala_convertida": destino
    }

    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True)