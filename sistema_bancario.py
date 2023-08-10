import re

regex_pattern_deposito = r'^\d+\.\d{2}$'

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
			saldo += valor_deposito
			registro_deposito = "\nDeposito {}\nSaldo {}"
			extrato += registro_deposito.format(valor_deposito, saldo)
			print(registro_deposito.format(valor_deposito, saldo))       			
		case "S":
			print("Sacar")				
						
		case "E":
			print("Extrato")
            
		case "Q":
			print("Sair")		
			exit();
		case _:
			print("opcao invalida")
		
	