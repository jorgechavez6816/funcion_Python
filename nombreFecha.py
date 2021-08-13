#p_date es la fecha a evaluar
#p_what es el pedido especifico, sea 'S' para semana o 'M' para mes.

def nombreFecha(p_date,p_what):
	from datetime import datetime
	temp= '19000101'
	if p_date > temp:
		temp= p_date
	xdate=datetime.strptime(temp,'%Y%m%d')
	if p_what.upper() == 'S':
		retval=xdate.strftime('%A')
	elif p_what.upper() == 'M':
		retval=xdate.strftime('%B')
	else:
		retval='Error'
	return retval
