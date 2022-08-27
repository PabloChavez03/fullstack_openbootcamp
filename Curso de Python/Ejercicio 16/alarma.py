def alarma(hora, minutos, segundos):
    if (hora >= 19):
        return 'Ya has salido de trabajar'
    else:
        hour = 19 - hora
        minutes = 60 - minutos
        seconds = 60 - segundos
        return 'Aun te falta ' + str(hour) + ":" + str(minutes) + ":" + str(seconds) + " para salir de trabajar"
