from fasthtml import FastHTML
from pathlib import Path
from fasthtml.common import *
from monsterui.all import *

from app.tickets import consultar_tickets
from app.database import  session
from app.models import Tickets

hdrs = (Theme.blue.headers())

app, rt = fast_app(hdrs=hdrs)

@dataclass
class New_Ticket:
    titulo: str
    departmento: str
    estado: str
    descripcion: str

@rt('/')
def index():
    return consultar_tickets()

@rt("/register")
def post(ticket: New_Ticket):
    valores = ticket.__dict__
    
    ticket = Tickets(
        id_ticket = 'TK-1002',
        titulo = valores['titulo'],
        descripcion = valores['descripcion'],
        estado = valores['estado'],
        departmento = valores['departmento'],
        )
    session.add(ticket)
    session.commit()

serve()