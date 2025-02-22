from fasthtml import FastHTML
from pathlib import Path
from fasthtml.common import *
from monsterui.all import *

from app.tickets import consultar_tickets
from app.database import  session
from app.models import Tickets, new_ticket, update_ticket, delete_ticket

valor_status = {1: "Creado", 2: "En revisión", 3: "En proceso", 4: "Resuelto"}

hdrs = (Theme.blue.headers())

app, rt = fast_app(hdrs=hdrs)

@dataclass
class New_Ticket:
    titulo: str
    departmento: str
    estado: str
    descripcion: str

@dataclass
class Update_Ticket:
    id: str
    titulo: str
    departmento: str
    estado: str
    step: str
    descripcion: str

@dataclass
class Delete_Ticket:
    id: str

@rt('/')
def index():
    return consultar_tickets()

@rt("/register")
def post(ticket: New_Ticket):
    valores = ticket.__dict__
    new_ticket(valores)
    #Toast(DivLAligned(UkIcon('check-circle', cls='mr-2'), "Ticket creado correctamente!"), id="success-toast", alert_cls=AlertT.success, cls=(ToastHT.end, ToastVT.bottom)),

@rt("/update")
def post(ticket: Update_Ticket):
    valores = ticket.__dict__
    valores.update(id=int(valores['id'].removeprefix('TK-')))
    valores.update(step=list(valor_status.keys())[list(valor_status.values()).index(valores['step'])])
    update_ticket(valores)

@rt("/borrar")
def post(ticket: Delete_Ticket):
    valores = ticket.__dict__
    valores.update(id=int(valores['id'].removeprefix('TK-')))
    delete_ticket(valores)

serve()