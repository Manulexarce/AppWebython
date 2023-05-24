from flask import Flask, render_template
import matplotlib.pyplot as plt
app = Flask(__name__, static_folder='static')



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/cargar')
def carga():
    return render_template('cargar.html')

@app.route('/footer')
def pagina2():
    return render_template('footer.html')


@app.route('/grafico')
def grafico():
    # Datos de temperatura
    temp = [23, 24, 25, 27, 26, 25, 24]

    # Crear un gráfico de líneas
    plt.plot(temp)

    # Guardar el gráfico en un archivo PNG
    plt.savefig('static/grafico.png')
    

    # Renderizar la plantilla que muestra el gráfico
    return render_template('grafico.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 