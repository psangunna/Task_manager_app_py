from models import *
import db
import datetime
def checkFormat_date(time=None):

    error = False

    time = str(time)

    try:
        transaction_date = datetime.datetime.strptime(time,"%d.%m.%Y")
    except ValueError:
        error = True

    return error

def validar_info(tarea):
    error = False
    if len(tarea.contenido) == 0:
        error = True
    if len(tarea.fecha_limite) != 10:
        error = True
    else:

        error = checkFormat_date(tarea.fecha_limite)


    if len(tarea.categoria) == 0 :
        error = True

    return error

def get_tarea_by_id(tarea_id):
    """Método para obtner ideas por id"""
    tarea = db.session.query(Tarea).filter_by(id_tarea=tarea_id).first()
    return tarea


def update_tarea_db(tarea_data):
    """Method that updates tasks"""

    tarea = get_tarea_by_id(tarea_data['id_tarea'])

    tarea.contenido = tarea_data['contenido']
    tarea.categoria = tarea_data['categoria']
    tarea.fecha_limite = tarea_data["fecha_limite"]
    #tarea.hecha = tarea_data["hecha"]


    db.session.commit()
