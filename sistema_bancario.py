import re

def faz_deposito(valor_deposito):
	global extrato
	global saldo

	saldo += valor_deposito
	registro_deposito = "\nDeposito {}\nSaldo {}"
	extrato += registro_deposito.format(valor_deposito, saldo)
	print(registro_deposito.format(valor_deposito, saldo)) 

def faz_saque():
	global saldo
	global extrato

	numero_saques += 1
	saldo -= valor_saque
	registro_deposito = "\nSaque {}\nSaldo {}"
	extrato += registro_deposito.format(valor_saque, saldo)
	print(registro_deposito.format(valor_saque, saldo))				
	
regex_pattern_deposito = r'^\d+\.\d{2}$'
regex_pattern_saque = r'^\d+$'

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
	
	opcao = input(menu)
	
	match opcao.upper():
		case "D":
			print("Deposito")
			valor_validado = False
			valor_deposito = 0.0
			while not valor_validado:
				valor_deposito_str = input("Por favor, informe o valor de depósito no formato XXXXX.XX :")
				if re.match(regex_pattern_deposito,valor_deposito_str):
					valor_deposito = float(valor_deposito_str)
					valor_validado = True					
			faz_deposito(valor_deposito)      			
		case "S":
			print("Sacar")		
			if numero_saques == LIMITE_SAQUES:
				print("limite diario de saques excedido (%d)",LIMITE_SAQUES)
			else:
				valor_saque = input
				valor_validado = False
				while not valor_validado:
					valor_saque_str = input("Por favor, informe o valor de depósito no formato XXXXX :")
					if re.match(regex_pattern_saque,valor_saque_str):
						valor_saque = int(valor_saque_str)
						valor_validado = True
						if valor_saque > 500:
							print("Valor acima do limite permitido (500)")
							valor_validado = False
						elif valor_saque <= 0:
							print("Valor negativo ou zero")
							valor_validado = False	
				faz_saque(valor_saque)		
		case "E":
			print("Extrato")
			print(extrato)            
		case "Q":
			print("Sair")		
			exit();
		case _:
			print("opcao invalida")
		
	