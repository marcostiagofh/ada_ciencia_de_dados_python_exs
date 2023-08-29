import re

def faz_deposito(saldo, extrato, valor_deposito):
	saldo += valor_deposito
	registro_deposito = "\nDeposito {}\nSaldo {}"
	extrato += registro_deposito.format(valor_deposito, saldo)
	print(registro_deposito.format(valor_deposito, saldo)) 

	return saldo, extrato

def faz_saque(saldo, extrato, valor_saque, limite, numero_saques, limite_saques):
	if numero_saques == limite_saques:
		print("limite diario de saques excedido (%d)",limite_saques)
	else:			
		numero_saques += 1
		saldo -= valor_saque
		registro_deposito = "\nSaque {}\nSaldo {}"
		extrato += registro_deposito.format(valor_saque, saldo)
		print(registro_deposito.format(valor_saque, saldo))				

	return saldo, extrato

def gera_extrato(saldo, extrato):
	print(extrato)      

def criar_usuario(usuarios):
	nome = input("Por favor, digite o nome :")
	
	dt_nasc_validado = False
	while not dt_nasc_validado:
		dt_nasc = input("Por favor, digite a data de nascimento, no formato dd/mm/aaaa :")
		if re.match("^(0[1-9]|[12]\d|3[01])\/(0[1-9]|1[0-2])\/\d{4}$",dt_nasc):
			dt_nasc_validado = True
		else:
			print("data de nascimento com formatacao errada! tente novamente.")
	
	cpf_validado = False
	while not cpf_validado:
		cpf = input("Por favor, digite o cpf com apenas digitos :")
		if re.match("^\d{11}$",cpf):
			cpf_validado = True
		else:
			print("CPF com formatacao errada! tente novamente.")
	
	endereco_validado = False
	while not endereco_validado:
		endereco = input("Por favor, digite a data de nascimento, no formato logradouro, numero - bairro - cidade/sigla estado :")
		if re.match("^(.*?), (\d+) - (.*?) - (.*?)\/([A-Z]{2}) ([A-Z][a-z]+)$",endereco):
			endereco_validado = True
		else:
			print("Endereco com formatacao errada! tente novamente.")
	
	if cpf in usuarios:
		print("Erro! usuario ja cadastrado")		
	else:
		usuarios[cpf] = {
			"nome":nome,
			"dt_nasc": dt_nasc,
			"endereco": endereco
		}

	return usuarios

def criar_conta_corrente(cpf, num_conta, contas_correntes):
	agencia = "0001"
	usuario = cpf

    if num_conta in contas_correntes:
		print("Erro! Conta ja cadastrada.")
    else:
		contas_correntes[num_conta] = {
			"agencia": agencia
			"usuario": cpf
		}
	
	return contas_correntes

def listar_contas(usuarios,contas_correntes):
	for u in usuarios:
		print("Nome",u["nome"],"CPF",u)
		print("contas")
		for c in contas_correntes:
			if c["usuario"] == u:
				print("Agencia", c["agencia"], "Conta", c)

regex_pattern_deposito = r'^\d+\.\d{2}$'
regex_pattern_saque = r'^\d+$'

menu = """
[u] Criar Usuario
[c] Criar Conta Corrente
[d] Depositar
[s] Sacar
[l] Lista Contas
[e] Extrato
[q] Sair

=> """
usuarios = {}
contas_correntes = {}
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
	
	opcao = input(menu)
	
	match opcao.upper():
		case "U":
			print("Criar Usuario")
			usuarios = criar_usuario(usuarios)
		case "C":
			print("Criar conta corrente")
			num_conta = len(contas_correntes)+1
			cpf = input("Por favor, digite o cpf com apenas digitos :")
		    contas_correntes = criar_conta_corrente(cpf, num_conta, contas_correntes)
		case "L":
			print("Lista contas")
			listar_contas(usuarios,contas_correntes)
		case "D":
			print("Deposito")
			valor_validado = False
			while not valor_validado:
				valor_deposito_str = input("Por favor, informe o valor de depósito no formato XXXXX.XX :")
				if re.match(regex_pattern_deposito,valor_deposito_str):
					valor_deposito = float(valor_deposito_str)
					valor_validado = True					
			faz_deposito(saldo, extrato, valor_deposito)

		case "S":
			print("Sacar")	
			valor_saque = input
			valor_validado = False
			while not valor_validado:
				valor_saque_str = input("Por favor, informe o valor de saque no formato XXXXX :")
				if re.match(regex_pattern_saque,valor_saque_str):
					valor_saque = int(valor_saque_str)
					valor_validado = True
					if valor_saque > 500:
						print("Valor acima do limite permitido (500)")
						valor_validado = False
					elif valor_saque <= 0:
						print("Valor negativo ou zero")
						valor_validado = False	
			faz_saque(saldo=saldo, extrato=extrato, valor_saque=valor_saque, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)		
		case "E":
			print("Extrato")
			gera_extrato(saldo, extrato=extrato)   
		case "Q":
			print("Sair")		
			exit();
		case _:
			print("opcao invalida")
		
	