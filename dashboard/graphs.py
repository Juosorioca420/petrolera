import pandas as pd
from django.db import connection
import plotly.express as px
from django.db.models import Sum
from .models import Factura

def valor():
    row = Factura.objects.values('acta__month', 'acta__year').annotate( total = Sum('valor') )
    df = pd.DataFrame(row)

    df['acta__year'] = df['acta__year'].astype(str)
    df['acta__month'] = df['acta__month'].astype(str).str.zfill(2)  # zfill para agregar un cero al inicio 
    df['fecha'] = df['acta__year'] + df['acta__month'] 
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y%m')

    df = df.sort_values('fecha')
    df['avg'] = df['total'].expanding().mean()

    fig = px.line()
    fig.add_scatter( x = df['fecha'], y = df['avg'], name = 'Promedio Acumulado'
                    , mode = 'lines', line_shape = 'spline', line_color = 'red' )
    
    fig.add_scatter( x = df['fecha'], y = df['total'], name = 'Regalia Mensual'
                    , mode = 'lines', line_shape = 'spline', fill = 'tonexty'
                    , line_color = 'indigo' )
    
    fig.update_layout( xaxis_title = 'Fecha',
                       yaxis_title = 'COP',
                       title = 'Total Regalias Mensuales en el Tiempo')

    return fig.to_html()

def territorios_graph():
    row = Factura.objects.values('campo__territorio__name').annotate( total = Sum('valor') )
    df = pd.DataFrame(row)
    df.rename( columns = {'campo__territorio__name':'name'}, inplace = True)

    fig = px.bar(df, y = 'name', x = 'total', text_auto= True
                 , orientation = 'h' )
    
    fig.update_layout( yaxis_title = 'Territorio', yaxis={'categoryorder': 'total ascending'},
                       xaxis_title = 'COP',
                       title = 'Total Regalias por Departamento')

    return fig.to_html()

def crudo_graph():
    row = Factura.objects.values('campo__crudo_name').annotate( total = Sum('valor') )
    df = pd.DataFrame(row)
    df.rename( columns = {'campo__crudo_name':'name'}, inplace = True)

    fig = px.bar(df, x = 'name', y = 'total')
    fig.update_traces(marker_color='darkorange')

    fig.update_layout( xaxis_title = 'Crudo',
                       yaxis_title = 'COP',
                       title = 'Total Regalias por Tipo de Crudo')

    return fig.to_html()

def operador_graph():
    row = Factura.objects.values('campo__operador__name').annotate( total = Sum('valor') )
    df = pd.DataFrame(row)
    df.rename( columns = {'campo__operador__name':'name'}, inplace = True)

    fig = px.bar(df, x = 'name', y = 'total')
    fig.update_traces(marker_color='mediumaquamarine')

    fig.update_layout( xaxis_title = 'Operador',
                       yaxis_title = 'COP',
                       title = 'Total Regalias por Operador')

    return fig.to_html()