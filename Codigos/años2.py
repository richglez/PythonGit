def saltoaño(año):
	if año % 4 != 0:
		return False
	elif año % 100 != 0:
		return True
	elif año % 400 != 0:
		return False
	else:
		return True

def diasEnMeses(año,mes):
	if año < 1582 or mes < 1 or mes > 12:
		return None
	dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = dias[mes - 1]
	if mes == 2 and saltoaño(año):
		res = 29
	return res

testaños = [1900, 2000, 2016, 1987]
testmeses = [ 2, 2, 1, 11]
testresultados = [28, 29, 31, 30]
for i in range(len(testaños)):
	añ = testaños[i]
	me = testmeses[i]
	print(añ,me,"-> ",end="")
	resultado = diasEnMeses(añ, me)
	if resultado == testresultados[i]:
		print("OK")
	else:
		print("Error")