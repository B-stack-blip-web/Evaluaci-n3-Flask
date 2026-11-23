from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "clave-local-ta6"


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        try:
            nota1 = float(request.form["nota1"])
            nota2 = float(request.form["nota2"])
            nota3 = float(request.form["nota3"])
            asistencia = float(request.form["asistencia"])

            if not all(10 <= n <= 70 for n in (nota1, nota2, nota3)):
                raise ValueError("Las notas deben estar entre 10 y 70.")
            if not 0 <= asistencia <= 100:
                raise ValueError("La asistencia debe estar entre 0 y 100.")

            promedio = (nota1 + nota2 + nota3) / 3
            aprobado = promedio >= 40 and asistencia >= 75

            return render_template(
                "ejercicio1.html",
                promedio=round(promedio, 2),
                asistencia=asistencia,
                aprobado=aprobado
            )
        except (ValueError, KeyError):
            flash("Ingresa valores válidos: notas entre 10 y 70 y asistencia entre 0 y 100.")
            return redirect(url_for("ejercicio1"))

    return render_template("ejercicio1.html")


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    if request.method == "POST":
        nombres = [
            request.form.get("nombre1", "").strip(),
            request.form.get("nombre2", "").strip(),
            request.form.get("nombre3", "").strip()
        ]

        if any(not nombre for nombre in nombres):
            flash("Debes completar los tres nombres.")
            return redirect(url_for("ejercicio2"))

        if len(set(nombre.casefold() for nombre in nombres)) != 3:
            flash("Debes ingresar tres nombres diferentes.")
            return redirect(url_for("ejercicio2"))

        mayor = max(len(nombre) for nombre in nombres)
        nombres_mayores = [nombre for nombre in nombres if len(nombre) == mayor]

        return render_template(
            "ejercicio2.html",
            nombres_mayores=nombres_mayores,
            cantidad=mayor
        )

    return render_template("ejercicio2.html")


if __name__ == "__main__":
    app.run(debug=True)
