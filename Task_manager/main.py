from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from flask import Flask, render_template,request, redirect, url_for, flash
import db
from models import Tarea
from form import tareaForm
from services import get_tarea_by_id, update_tarea_db,checkFormat_date, validar_info
from utils import get_dict_from_wftform

# Create an instance of the Flask class
app = Flask(__name__)
bootstrap = Bootstrap(app)
fa = FontAwesome(app)
app.config['SECRET_KEY'] = 'any secret string'


def contextHome():

    tarea_form = tareaForm()

    context = {
        "tarea_form" : tarea_form,
        "modal": {
            "update": False

        },
    }
    return context

@app.route("/", methods=['GET', 'POST'])
def index():
    error = False
    context = contextHome()
    tarea_form = context["tarea_form"]
    todas_las_tareas = db.session.query(Tarea).all()

    for i in todas_las_tareas:
        print(i)

    context = {
        "lista_de_tareas" : todas_las_tareas,
        "tarea_form": tarea_form,
        "modal": {
            "update": False

            },
        }

    if tarea_form.validate_on_submit():
        form_dict = get_dict_from_wftform(tarea_form)
        if tarea_form.id_tarea.data != '':
            error = checkFormat_date( tarea_form.fecha_limite.data)
            if error == False:
                update_tarea_db(form_dict)
                flash("Data updated successfully", category="sucess")
            else:
                flash("The deadline has not been provided in the correct format", category="error")

            return redirect(url_for("index"))

    return render_template("index.html", **context)

@app.route("/crear-tarea", methods = ["POST"])
def crear():

    tarea = Tarea(contenido = request.form["contenido_tarea"],categoria = request.form["categoria_tarea"],fecha_limite = request.form["fecha_tarea"],hecha = False)

    error = validar_info(tarea)
    if error == False:
        db.session.add(tarea)
        db.session.commit()
        flash("Task created", category="sucess")
    else:
        flash( "Data has not been provided in the correct format", category = "error")

    return redirect(url_for("index")) #"Tarea guardada"

@app.route("/eliminar-tarea/<id>") #id -->identificar cual vamos a eliminar
def eliminar(id):
    tarea = db.session.query(Tarea).filter_by(id_tarea = id).delete()
    db.session.commit()
    flash("Task deleted", category="info")
    return redirect(url_for("index"))

#id -->identify which task will be eliminated
@app.route("/tarea-hecha/<id>")
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id_tarea = id).first()
    tarea.hecha = not(tarea.hecha)
    db.session.commit()
    flash("Task completed", category="info")
    return redirect(url_for("index"))


#id -->identify which task will be edited
@app.route("/editar-tarea/<id>", methods=['GET', 'POST'])
def editar(id):
    todas_las_tareas = db.session.query(Tarea).all()
    lista_de_tareas =  todas_las_tareas
    context = contextHome()

    tarea_form = context["tarea_form"]

    tarea = get_tarea_by_id(id) # get the task
    tarea_form.id_tarea.data = tarea.id_tarea  # render task into the form
    tarea_form.contenido.data = tarea.contenido
    tarea_form.categoria.data = tarea.categoria
    tarea_form.fecha_limite.data = tarea.fecha_limite
    tarea_form.hecha.data = tarea.hecha

    context['tarea_form'] = tarea_form
    context['modal'] = {
       "update": True

    }
    context['lista_de_tareas'] = lista_de_tareas

    return render_template('index.html', **context)



@app.route('/cerrar')
def cerrar():

    return redirect(url_for("index"))


if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
    app.run(debug = True)
