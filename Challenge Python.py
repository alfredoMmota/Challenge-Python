# -*- coding: utf-8 -*-
"""
@author: Jose Alfredo Mendoza Mota
"""
import time
from datetime import date, timedelta
import pandas_datareader.data as web
import webbrowser
from win10toast_click import ToastNotifier 


def open_url():
    try:
        webbrowser.open_new(page_url)
        print('Opening URL...')  
    except: 
        print('Failed to open URL. Unsupported variable type.')

def notificacion(bolsa,variacion=0):
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
    page_url = 'https://smartrader.io/'
    toaster = ToastNotifier()
    # hoy = date.today()
    hoy = date.today()-timedelta(days = 1)
    ayer = date.today()-timedelta(days = 2)
    nikkey25 = web.DataReader("^N225", "yahoo", ayer, hoy)
    dax = web.DataReader("^DAX-EU", "yahoo", ayer, hoy)
    nasdaq =  web.DataReader("^IXIC", "yahoo", ayer, hoy)
    PrecioInicialNikkey = nikkey25.loc[ayer,"Adj Close"]
    PrecioInicialDax = dax.loc[hoy,"Adj Close"]
    PrecioInicialNasdaq = nasdaq.loc[ayer,"Adj Close"]
    
    while True:
        variacion_Nikkey = PrecioInicialNikkey * 0.05
        variacion_Dax = PrecioInicialDax * 0.05
        variacion_Nasdaq = PrecioInicialNasdaq * 0.05
        nikkey25 = web.DataReader("^N225", "yahoo",ayer, hoy)
        dax = web.DataReader("^DAX-EU", "yahoo",ayer, hoy)
        nasdaq =  web.DataReader("^IXIC", "yahoo",ayer, hoy)
        PrecioActualNikkey = nikkey25.loc[hoy,"Adj Close"]
        PrecioActualDax = dax.loc[hoy,"Adj Close"]
        PrecioActualNasdaq = nasdaq.loc[hoy,"Adj Close"]
        Diferencia_Nikkey = PrecioInicialNikkey - PrecioActualNikkey
        Diferencia_Dax = PrecioInicialDax - PrecioActualDax
        Diferencia_Nasdaq = PrecioInicialNasdaq - PrecioActualNasdaq
        if Diferencia_Nikkey > variacion_Nikkey:
            notificacion("Nikkey 225", 1)
        elif Diferencia_Nikkey < (variacion_Nikkey * -1):
            notificacion("Nikkey 225", 2)
        else:
            notificacion("Nikkey 225")
        time.sleep(5)
        if Diferencia_Dax > variacion_Dax:
            notificacion("Dax", 1)
        elif Diferencia_Dax < (variacion_Dax * -1):
            notificacion("Dax", 2)
        else:
            notificacion("Dax")
        time.sleep(5)
        if Diferencia_Nasdaq > variacion_Nasdaq:
            notificacion("Nasdaq", 1)
        elif Diferencia_Nasdaq < (variacion_Nasdaq * -1):
            notificacion("Nasdaq", 2)
        else:
            notificacion("Nasdaq")
        time.sleep(5)
        PrecioInicialNikkey = PrecioActualNikkey
        PrecioInicialDax = PrecioActualDax
        PrecioInicialNasdaq = PrecioActualNasdaq
