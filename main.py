from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# ---------- EJERCICIO 1 ----------
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    promedio = None
    estado_curso = None

    if request.method == "POST":
        nota1 = float(request.form["nota1"])
        nota2 = float(request.form["nota2"])
        nota3 = float(request.form["nota3"])
        asistencia = float(request.form["asistencia"])

        promedio = (nota1 + nota2 + nota3) / 3

        if promedio >= 40 and asistencia >= 75:
            estado_curso = "APROBADO"
        else:
            estado_curso = "REPROBADO"

    return render_template(
        "ejercicio1.html",
        promedio=promedio,
        estado=estado_curso
    )

# ---------- EJERCICIO 2 ----------
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    nombre_largo = None
    cantidad = None

    if request.method == "POST":
        nombre1 = request.form["nombre1"]
        nombre2 = request.form["nombre2"]
        nombre3 = request.form["nombre3"]

        nombres = [nombre1, nombre2, nombre3]
        nombre_largo = max(nombres, key=len)
        cantidad = len(nombre_largo)

    return render_template(
        "ejercicio2.html",
        nombre=nombre_largo,
        cantidad=cantidad
    )

if __name__ == "__main__":
    app.run(debug=True)
