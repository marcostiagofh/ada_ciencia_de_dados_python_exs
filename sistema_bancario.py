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
			
		case "S":
			print("Sacar")				
						
		case "E":
			print("Extrato")
            
		case "Q":
			print("Sair")		
			exit();
		case _:
			print("opcao invalida")
		
	