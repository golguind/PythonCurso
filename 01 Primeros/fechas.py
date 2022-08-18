from datetime import date, timedelta, datetime
fecha = date.today() - timedelta(days=7) 
format = fecha.strftime('%Y-%m-%d')
print (fecha)
print (format)





now = datetime.now()
format = now.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')

print(format)

def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    segundo = 5804 
    messsage = "{} de {} del {} de numero {}".format(day, month, year, segundo)

    return messsage

now = datetime.now()
print(current_date_format(now))