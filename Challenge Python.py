# -*- coding: utf-8 -*-
"""
@author: Jose Alfredo Mendoza Mota
"""
#Se importan las librerias
import time
from datetime import date, timedelta
import pandas_datareader.data as web
import webbrowser
from win10toast_click import ToastNotifier 


def open_url():# Funcion que abre el enlace a la pagina https://smartrader.io/
    try:
        webbrowser.open_new(page_url)
    except: 
        print('URL erroneo')

def notificacion(bolsa,variacion=0):#Funcion que despliega la notificación en el sistema
    if variacion == 1 and bolsa == 'Nikkey 225':
            toaster.show_toast("Cambio en los valores de la bolsa ",bolsa,
                   "El valor del mercado ha aumentado",
                   duration=20,
                   threaded=True,
                   callback_on_click=open_url)
    elif variacion == 1 and bolsa == 'Dax':
            toaster.show_toast("Cambio en los valores de la bolsa ",bolsa,
                   "El valor del mercado ha aumentado",
                   duration=20,
                   threaded=True,
                   callback_on_click=open_url)
    elif variacion == 1 and bolsa == 'Nasdaq':
            toaster.show_toast("Cambio en los valores de la bolsa ",bolsa,
                   "El valor del mercado ha aumentado",
                   duration=20,
                   threaded=True,
                   callback_on_click=open_url)
    elif variacion == 2 and bolsa == 'Nikkey 225':
        toaster.show_toast("Cambio en los valores de la bolsa ",bolsa,
                   "El valor del mercado ha disminuido",
                   duration=20,
                   threaded=True,
                   callback_on_click=open_url)
    elif variacion == 2 and bolsa == 'Dax':
        toaster.show_toast("Cambio en los valores de la bolsa ",bolsa,
                   "El valor del mercado ha disminuido",
                   duration=20,
                   threaded=True,
                   callback_on_click=open_url)
    elif variacion == 2 and bolsa == 'Nasdaq':
        toaster.show_toast("Cambio en los valores de la bolsa ",bolsa,
                   "El valor del mercado ha disminuido",
                   duration=20,
                   threaded=True,
                   callback_on_click=open_url)
    else:
        toaster.show_toast("Cambio en los valores de la bolsa {}".format(bolsa),
                   "El valor del mercado continua estable",
                   duration=10)
    
if __name__ == "__main__":
    page_url = 'https://smartrader.io/' #Se define la url de la pagina
    toaster = ToastNotifier() #se define el notificador
    hoy = date.today() # se obtiene la fecha actual
    ayer = date.today()-timedelta(days = 1)# se obtiene la fecha de cierre del dia anterior
    #Se realizan las primeras lecturas de los datos de las bolsas de valores Nikkey 225, Dax Index y Nasdaq
    nikkey25 = web.DataReader("^N225", "yahoo", ayer, hoy)
    dax = web.DataReader("^DAX-EU", "yahoo", ayer, hoy)
    nasdaq =  web.DataReader("^IXIC", "yahoo", ayer, hoy)
    #Se almacena el valor de cierre
    PrecioInicialNikkey = nikkey25.loc[ayer,"Adj Close"]
    PrecioInicialDax = dax.loc[ayer,"Adj Close"]
    PrecioInicialNasdaq = nasdaq.loc[ayer,"Adj Close"]
    
    while True:#se crea un ciclo para mantener ejecutando la comparacion de valores
        #se obtiene el valor de variacion de las bolsas de valores el cual es del 0.5%
        variacion_Nikkey = PrecioInicialNikkey * 0.05
        variacion_Dax = PrecioInicialDax * 0.05
        variacion_Nasdaq = PrecioInicialNasdaq * 0.05
        #Se realizan lecturas de los datos de las bolsas de valores en la fecha actual
        nikkey25 = web.DataReader("^N225", "yahoo",ayer, hoy)
        dax = web.DataReader("^DAX-EU", "yahoo",ayer, hoy)
        nasdaq =  web.DataReader("^IXIC", "yahoo",ayer, hoy)
        #Se almacenan los valores actuales de los mercados
        PrecioActualNikkey = nikkey25.loc[hoy,"Adj Close"]
        PrecioActualDax = dax.loc[hoy,"Adj Close"]
        PrecioActualNasdaq = nasdaq.loc[hoy,"Adj Close"]
        #se determina la diferecia que existe entre el valor anterior y el valor actual
        Diferencia_Nikkey = PrecioInicialNikkey - PrecioActualNikkey
        Diferencia_Dax = PrecioInicialDax - PrecioActualDax
        Diferencia_Nasdaq = PrecioInicialNasdaq - PrecioActualNasdaq
        """
        Se realizan las comparaciones, las cuales determinan si el mercado subio o bajo
        basado en el resultado se llama a la funcion que despliega la notificacion en el
        Sistema
        """
        if Diferencia_Nikkey > variacion_Nikkey:
            notificacion("Nikkey 225", 1)
        elif Diferencia_Nikkey < (variacion_Nikkey * -1):
            notificacion("Nikkey 225", 2)
        else:
            notificacion("Nikkey 225")
        time.sleep(10)
        if Diferencia_Dax > variacion_Dax:
            notificacion("Dax", 1)
        elif Diferencia_Dax < (variacion_Dax * -1):
            notificacion("Dax", 2)
        else:
            notificacion("Dax")
        time.sleep(10)
        if Diferencia_Nasdaq > variacion_Nasdaq:
            notificacion("Nasdaq", 1)
        elif Diferencia_Nasdaq < (variacion_Nasdaq * -1):
            notificacion("Nasdaq", 2)
        else:
            notificacion("Nasdaq")
        #Se determina el lapso de tiempo para cada una de las lecturas y comparación (7200 segundos = 2 hrs)
        time.sleep(7200)
        #Se actualizan los precios con la ultima lectura realizada
        PrecioInicialNikkey = PrecioActualNikkey
        PrecioInicialDax = PrecioActualDax
        PrecioInicialNasdaq = PrecioActualNasdaq
