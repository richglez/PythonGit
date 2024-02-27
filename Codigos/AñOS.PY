def saltoaño(año):
	if año % 4 != 0:
		return False
	elif año % 100 != 0:
		return True
	elif año % 400 != 0:
		return False
	else:
		return True

test = [1900, 2000, 2016, 1987]
testresultados = [False, True, True, False]
for i in range(len(test)):
	yr = test[i]
	print(yr,"-> ",end="")
	resultado = saltoaño(yr)
	if resultado == testresultados[i]:
		print("OK")
	else:
		print("Error")