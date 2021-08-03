def obtenerPorcentaje(numerator, denominator):
	if(denominator == 0):
		return "N/A"
	return "{0:.2f} %".format(numerator/denominator*100)


