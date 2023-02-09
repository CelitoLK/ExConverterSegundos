valor = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dias = valor // 86400
segundosRestantes = valor % 86400
horas= segundosRestantes // 3600 
segundosRestantesFim = segundosRestantes % 3600
min = segundosRestantesFim // 60
seg = segundosRestantesFim % 60

print('{} dias, {} horas, {} minutos e {} segundos.'.format(dias, horas, min, seg))