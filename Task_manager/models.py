from sqlalchemy import Column, Integer, String, Boolean
import db


class Tarea(db.Base):
    __tablename__ = "tarea"  # ORM : table name
    __table_args__ = {'sqlite_autoincrement': True}  # auto. primary key
    id_tarea = Column(Integer, primary_key=True)
    contenido = Column(String(200), nullable=False)
    categoria = Column(String(100), nullable=False)
    fecha_limite = Column(String(20), nullable=False)
    hecha = Column(Boolean)

    def __init__(self, contenido, hecha, categoria, fecha_limite):
        self.contenido = contenido
        self.hecha = hecha
        self.categoria = categoria
        self.fecha_limite = fecha_limite

    def __str__(self):

        return "Tarea: {} -> {} -> {} -> {} -> {}".format(self.id_tarea, self.contenido, self.categoria,
                                                          self.fecha_limite, self.hecha)