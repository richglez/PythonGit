def saltoaño(año):
	if año % 4 != 0:
		return False
	elif año % 100 != 0:
		return True
	elif año % 400 != 0:
		return False
	else:
		return True

def diasEnMeses(año, mes):
	if año < 1582 or mes < 1 or mes > 12:
		return None
	dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = dias[mes - 1]
	if mes == 2 and saltoaño(año):
		res = 29
	return res

def diasDelAño(año, mes, dia):
	dias = 0
	for m in range(1, mes):
		md = diasEnMeses(año, m)
		if md == None:
			return None
		dias += md
	md = diasEnMeses(año, mes)
	if dia >= 1 and dia <= md:
		return dias + dia
	else:
		return None

print(diasDelAño(2000, 12, 31))