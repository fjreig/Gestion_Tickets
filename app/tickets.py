
from fasthtml.common import *
from monsterui.all import *
from datetime import datetime

from app.models import get_all_tickets

app, rt = fast_app(hdrs=Theme.blue.headers(daisy=True))

def TicketSteps(step):
    return Steps(
        LiStep("Creado", data_content="📝",
               cls=StepT.success if step > 0 else StepT.primary if step == 0 else StepT.neutral),
        LiStep("En revisión", data_content="🔎",
               cls=StepT.success if step > 1 else StepT.primary if step == 1 else StepT.neutral),
        LiStep("En proceso", data_content="⚙️",
               cls=StepT.success if step > 2 else StepT.primary if step == 2 else StepT.neutral),
        LiStep("Resuelto", data_content="✅",
               cls=StepT.success if step > 3 else StepT.primary if step == 3 else StepT.neutral),
        cls="w-full")

def StatusBadge(status):
    styles = {'Alta': AlertT.error, 'Media': AlertT.warning,'Baja': AlertT.info}
    alert_type = styles.get(status, AlertT.info)
    return Alert(f"Prioridad {status.title()}", cls=(alert_type,"w-32 shadow-sm"))

def TicketCard(id, title, description, status, step, department):
    return Card(
        CardHeader(
            DivFullySpaced(
                Div(H3(f"#{id}", cls=TextT.muted), 
                    H4(title), 
                    cls='space-y-2'),
                StatusBadge(status))),
        CardBody(
            P(description, cls=(TextT.muted, "mb-6")),
            DividerSplit(cls="my-6"),
            TicketSteps(step),
            DividerSplit(cls="my-6"), 
            DivFullySpaced(
                Div(Strong("Department"),
                    P(department),
                    cls=('space-y-3', TextPresets.muted_sm)),
                Div(Strong("Last Updated"),
                    P(Time(datetime.now().strftime('%b %d, %H:%M'))),
                    cls=('space-y-2', TextPresets.muted_sm)),
                Button("Editar", cls=ButtonT.primary),
                Button("Borrar", cls=ButtonT.secondary),
                cls='mt-6')),
        cls=CardT.hover)

def NewTicketModal():
    return Modal(
        ModalHeader(H3("Crear nuevo ticket de Soporte")),
        ModalBody(
            Form(
                Grid(LabelInput("Titulo", id="title", placeholder="Breve descripción de la averia", name="titulo"),
                    LabelSelect(*map(Option,("IT Support", "HR", "Facilities", "Finance")), placeholder="Selecciona un departamento", label="Departamento",  id="department", name="departmento")),
                    LabelSelect(*map(Option,("Baja", "Media", "Alta")), placeholder="Selecciona un nivel de Prioridad", label="Nivel de Prioridad", id="priority", name="estado"),
                    LabelTextArea("Descripcion", id="description", placeholder="Descripcion detallada de la averia", name="descripcion"),
                    DivRAligned(
                        Button("Cancelar", cls=ButtonT.ghost, data_uk_toggle="target: #new-ticket"),
                        Button("Crear", cls=ButtonT.primary, data_uk_toggle="target: #success-toast; target: #new-ticket")
                ),
            hx_post="/register",
            cls='space-y-8')),
        id="new-ticket")

def consultar_tickets():
    tickets = get_all_tickets()
    return Title("Tablero gestion de Tickets"), Container(
        Section(
            DivFullySpaced(
                H2("Tickets Activos"),
                Button(UkIcon("plus-circle", cls="mr-2"), "Nuevo Ticket", cls=ButtonT.primary, data_uk_toggle="target: #new-ticket"),
                cls='mb-8'),
            Grid(*[TicketCard(**ticket) for ticket in tickets], cols=1),
            cls="my-6"),
        NewTicketModal(),
        #Toast(DivLAligned(UkIcon('check-circle', cls='mr-2'), "Ticket submitted successfully! Our team will review it shortly."), id="success-toast", alert_cls=AlertT.success, cls=(ToastHT.end, ToastVT.bottom)),
        Loading(htmx_indicator=True, type=LoadingT.dots, cls="fixed top-0 right-0 m-4"),
        cls="mx-auto max-w-7xl"
    )   