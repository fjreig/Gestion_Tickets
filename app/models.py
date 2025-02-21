from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy import Date, cast, extract, func
from datetime import datetime
from fasthtml.common import *

from app.database import Base, session, engine

@dataclass
class Tickets(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    fechacreacion = Column(DateTime, default=datetime.utcnow)
    fechamodificacion = Column(DateTime, default=datetime.utcnow)
    id_ticket = Column(String)
    titulo = Column(String)
    descripcion = Column(String)
    estado = Column(String)
    step = Column(Integer, default=0)
    departmento = Column(String)

def get_all_tickets():
    result = session.query(Tickets).with_entities(
        Tickets.id_ticket.label('id'),
        Tickets.titulo.label('title'),
        Tickets.descripcion.label('description'),
        Tickets.estado.label('status'),
        Tickets.step.label('step'),
        Tickets.departmento.label('department')
        ).all()
    valores = []
    for i in range(len(result)):
        valores.append({
            'id': result[i][0], 
            'title': result[i][1],
            'description': result[i][2],
            'status': result[i][3],
            'step': int(result[i][4]),
            'department': result[i][5]
            })
    return(valores)