from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, Group
from .models import Factura, Indicador, Campo, Crudo, Carrotanque, HistoriaCarrotanque, Territorio, Puerto, Oleoducto, OleoductoAtraviesa
from .forms import IndicadorForm, FacturaForm, PromedioForm, CrudoForm, CarroForm, CapacidadForm, OperadorForm

from .graphs import valor, territorios_graph, crudo_graph, operador_graph

def root_redirect(request):
    # Redirigir a 'home' si el usuario está autenticado
    if request.user.is_authenticated: return redirect('index')  

    # Redirigir a 'login' si el usuario no está autenticado
    else: return redirect('login')  



# Create your views here.
@login_required
def index(request):
    # print(request.user.groups.filter(name='accountant').exists)
    fig1 = valor()
    fig2 = territorios_graph()
    fig3 = crudo_graph()
    fig4 = operador_graph()

    context = {
        'fig1' : fig1,
        'fig2' : fig2,
        'fig3' : fig3,
        'fig4' : fig4
    }
    return render(request, 'index.html', context)


@login_required
def facturas(request):

    facturas = Factura.objects.all().order_by('-acta__year', '-acta__month', '-id')
    total = 0
    for f in  facturas: total += f.valor
    total = f'{total:,}'

    if request.method == 'POST':
        factura_form = FacturaForm( request.POST )
        if factura_form.is_valid():
            campo = factura_form.cleaned_data.get('name')
            cantidad = factura_form.cleaned_data.get('cantidad')
            # print(campo, cantidad)

            if cantidad <= 0 : messages.error(request, f'La cantidad ingresada debe ser mayor a 0.')
            else:
                messages.info(request, f'Factura Añadida Existosamente.')
                crear_factura(campo, cantidad)

            return redirect( 'facturas' )

    else:
        factura_form = FacturaForm()

    avg_form = PromedioForm(request.GET)
    try:
        campo_avg = request.GET.get('name')
        campo_avg = Campo.objects.get(id = campo_avg).name
        avg = promedio_campo(campo_avg)
        avg = f'Promedio de produccion de {campo_avg}: {avg[0]:,}  COP'

    except:
        avg = None

    context = {
        'facturas' : facturas,
        'total' : total,
        'factura_form' : factura_form,
        'avg_form' : avg_form,
        'avg' : avg,
    }
    return render( request, 'facturas.html', context)

def delete_factura(request, pk):
    factura = Factura.objects.get(id = pk)

    if request.method == 'POST':
        factura.delete()
        return redirect('facturas')
    
    context = { 'factura': factura }
    return render(request, 'delete_factura.html', context)

# def edit_factura(request):

def crear_factura(campo, cantidad):
    with connection.cursor() as c:
        c.callproc('crear_factura', [campo, cantidad])

def promedio_campo(campo):
    q = '''SELECT fn_promCampo(%s) AS avg''';
    with connection.cursor() as c:
        c.execute(q, [campo])
        avg = c.fetchone()
    return avg
        

@login_required
def indicador(request):
    indicadores = Indicador.objects.all().order_by('id')

    if request.method == 'POST':
        indicador_form = IndicadorForm( request.POST )
        if indicador_form.is_valid():
            brent = indicador_form.cleaned_data.get('brent')
            trm = indicador_form.cleaned_data.get('TRM')

            messages.info(request, f'Registro Actualizado Existosamente.')

            update_indicadores(brent, trm)
            return redirect( 'indicador' )
    else: 
        indicador_form = IndicadorForm()

    context = {
        'indicadores' : indicadores,
        'indicador_form' : indicador_form,
    }
    return render( request, 'indicador.html', context)

def update_indicadores(brent, trm):
    with connection.cursor() as c:
        c.callproc('update_indicadores', [brent, trm])


@login_required
def acta(request):
    q = '''SELECT a.id, a.year, a.month, COUNT(f.id) as conteo_f, SUM(f.valor) as sum_f
            FROM acta a , factura f
            WHERE a.id = f.acta_id 
            GROUP BY a.id
            ORDER BY a.year DESC, a.month DESC''';
    
    with connection.cursor() as c:
        c.execute(q)
        actas = c.fetchall()
    # print(actas)

    if request.method == 'POST':
        operador_form = OperadorForm(request.POST)
        if operador_form.is_valid():
            operador = operador_form.cleaned_data.get('name')
            avg = promedio_operador(operador)

            if avg[0]:
                messages.warning(request, f'Valor promedio de regalias para {operador}: {avg[0]:,} COP')
            else:
                messages.error(request, f'No se tienen facturas registradas para {operador}')

            return redirect('acta')
    else:
        operador_form = OperadorForm()

    context = {
        'actas' : actas,
        'operador_form' : operador_form,
    }
    return render( request, 'acta.html', context )

def promedio_operador(operador):
    q = '''SELECT fn_promHistoricoOperador(%s) AS avg''';
    with connection.cursor() as c:
        c.execute(q, [operador])
        avg = c.fetchone()
    return avg


@login_required
def campo(request):
    campos = Campo.objects.all().order_by('name')
    crudos = Crudo.objects.all().order_by('name')

    if request.method == 'POST':
        crudo_form = CrudoForm( request.POST )
        if crudo_form.is_valid():
            current = crudo_form.cleaned_data.get('crudo_name')
            equiv = crudo_form.cleaned_data.get('equiv')
            equiv = round(equiv,3)

            print(current, equiv)

            if 0 < equiv <= 1 : 
                messages.info(request, f'Equivalencia Modificada Exitosamente')
                update_crudo_equiv(current, equiv)
            else:
                messages.error(request, f'Se admiten unicamente valores entre 0 y 1.')

            return redirect( 'campo' )

    else:
        crudo_form = CrudoForm()

    context = {
        'crudo_form' : crudo_form,
        'campos' : campos,
        'crudos' : crudos,
    }
    return render( request, 'campo.html', context )

def update_crudo_equiv(campo, equiv):
    with connection.cursor() as c:
        c.callproc('update_crudo_equiv', [campo, equiv])



@login_required
def carros( request ):
    historia = HistoriaCarrotanque.objects.all()
    carros = Carrotanque.objects.all()

    if request.method == 'POST':
        form = CarroForm(request.POST)
        if form.is_valid():
            matricula = form.cleaned_data.get('matricula')
            territorio = form.cleaned_data.get('name')

            current = Carrotanque.objects.get( id = matricula ).territorio_id
            current = Territorio.objects.get( id = current )
            # print(type(matricula), type(territorio), type(current))
            
            if current == territorio:
                messages.error(request, f'El Vehiculo ya se encuentra en {territorio}.')
            else:
                messages.info(request, f'Desplazamiento Registrado Exitosamente')
                asignar_carrotanque(matricula, territorio)
    else:
        form = CarroForm()

    capacidad_form = CapacidadForm(request.GET)
    try:
        territorio = request.GET.get('name')
        print(territorio)
        territorio = Territorio.objects.get(id = territorio).name
        print(territorio)
        capacidad = capacidad_carrotanques(territorio)
        capacidad = f'Disponibilidad en {territorio}: {capacidad[0]:,} lt'
    except:
        capacidad = None

    context = {
        'historia' : historia,
        'carros' : carros,
        'form' : form,
        'capacidad_form' : capacidad_form,
        'capacidad' : capacidad
    }
    return render( request, 'carrotanque.html', context)

def asignar_carrotanque(matricula, territorio):
    with connection.cursor() as c:
        c.callproc('asignar_carrotanque', [matricula, territorio]) 

def capacidad_carrotanques(territorio):
    q = '''SELECT fn_capacidadCarrotanques(%s) AS capacidad''';
    with connection.cursor() as c:
        c.execute(q, [territorio])
        capacidad = c.fetchone()
    return capacidad

def oleoducto(request):
    puertos = Puerto.objects.all()
    oleoductos = Oleoducto.objects.all().order_by('id')
    estaciones = OleoductoAtraviesa.objects.all()

    context = {
        'oleoductos' : oleoductos,
        'estaciones' : estaciones,
        'puertos' : puertos
    }
    return render( request, 'oleoducto.html', context )