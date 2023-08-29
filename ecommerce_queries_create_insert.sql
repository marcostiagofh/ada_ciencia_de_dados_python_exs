--criar tabela cliente
drop table clients;
CREATE TABLE clients(
	 idClient int auto_increment primary key,
	 Fname varchar(20),
	 Minit char(3),
	 Lname varchar(20),
	 CPF char(11),
	 CNPJ char(15) default null,
	 Address varchar(255),
	 constraint unique_cpf_clients unique (CPF),
	 constraint unique_cnpj_clients unique (CNPJ)
);

--criar tabela produto
CREATE TABLE products(
	idProduct int auto_increment primary key,
	nome varchar(45),
	classification_kids bool default false,
	category enum('Eletrônico','Vestimenta','Brinquedos','Alimentos','Móveis') ,
	rating float default 0,
	dimensions varchar(10)
);

--criar tabela pagamento
CREATE TABLE payments(
	idPayment int,
	idClient int,
	idPaymentType int,
	debtValue float,
	primary key(idClient, idPayment)
    constraint fk_payments_paymenttypes FOREIGN key (idPaymentType) references paymentTypes(idPaymentType)	
);

--criar tabela forma de pagamento
CREATE TABLE paymentTypes(
	idPaymentType int auto_increment primary key,
	typePayment enum('Boleto','Cartao de credito', 'Dois cartoes', 'Pix'),
	cardNumber char(16),
	expInMonth int,
	expInYear int,
	cvv char(3)	
);

--criar tabela pedido
CREATE TABLE orders(
	idOrder int auto_increment primary key,
	idClient int,
	orderStatus enum('Cancelado','Confirmado','Em processamento') not null default 'Em processamento',
	orderDescription varchar(255),
	transportFee float default 10,
	paymentCash bool default true,
	idPayment int default null,
	constraint fk_order_client FOREIGN key (idClient) references clients(idCliente),
	constraint fk_order_payment FOREIGN key (idClient, idPayment) references payments(idClient, idPayment)
);

--criar tabela estoque
CREATE TABLE productStorages(
	idProductStorage int auto_increment primary key,
	address varchar(30),
	quantity int default 0	
);

--criar tabela fornecedor
CREATE TABLE suppliers(
	idSupplier int auto_increment primary key,
	socialName varchar(255) not null,
	CNPJ char(15) not null,
	contact char(11) not null,
	constraint unique_supplier unique (CNPJ)
	
);

--criar tabela vendedor
-- criar tabela vendedor
CREATE TABLE sellers(
	idSeller int auto_increment primary key,
	socialName varchar(255) not null,
	AbstName varchar(255),
	CNPJ char(15),
	CPF char(11),
	address varchar(255),
	contact char(11) not null,
	constraint unique_cnpj_seller unique (CNPJ),
	constraint unique_cpf_seller unique (CPF)
);

-- criar tabela produto_vendedor
CREATE TABLE productSeller(
	idSeller int,
	idProduct int,
	quantity int default 1,
	primary key(idSeller, idProduct),
	constraint fk_productSeller_seller foreign key (idSeller) references sellers(idSeller),
	constraint fk_productSeller_product foreign key (idProduct) references products(idProduct)
);

-- criar tabela vendedor
CREATE TABLE productOrders(
	idProduct int,
	idOrder int,
	quantity int default 1,
	status enum('Disponível','Sem estoque') default 'Disponível',
	primary key(idProduct,idOrder),
	constraint fk_productOrders_product foreign key (idProduct) references products(idProduct),
	constraint fk_productOrders_order foreign key (idOrder) references orders(idOrder)
);

CREATE TABLE storageLocations(
	idProduct int,
	idProductStorage int,
	address varchar(255) not null,
	primary key(idProduct,idProductStorage),
	constraint fk_storageLocations_products foreign key (idProduct) references products(idProduct),
	constraint fk_storageLocations_productStorage foreign key (idProductStorage) references productStorages(idProductStorage)
);

CREATE TABLE productSupplier(
	idSupplier int,
	idProduct int,
	quantity int not null,
	primary key (idSupplier, idProduct),
	constraint fk_productSupplier_supplier foreign key (idSupplier) references suppliers(idSupplier),
	constraint fk_productSupplier_product foreign key (idProduct) references products(idProduct)
);

create table orders(
	...on update CASCADE
	on delete set null
)

insert into Clients (Fname, Minit, Lname, CPF, Address)
values ('Maria','M','Silva', 12346789,  'rua silva de prata 29, Carangola - Cidade das flores'),
('Matheus','O', 'Pimentel', 987654321,  'rua alameda 289, Centro - Cidade das flores'),
('Ricardo','F','Silva', 45678913,  'avenida alameda vinha 1009, Centro - Cidade das flores'),
('Julia', 'S', 'França', 789123456,  'rua laranjeiras 861, Centro - Cidade das flores'),
('Roberta','G','Assis', 98745631,  'avenida koller 19, Centro - Cidade das flores'),
('Isabella','M','Cruz', 654789123,  'rua alameda das flores 28, Centro - Cidade das flores');

insert into products(nome, classification_kids, category, rating, dimensions) values
('Fone de ouvido', false, 'Eletrônico','4',null),
('Barbie Elsa', true, 'Brinquedos','3',null),
('Body Carters', true, 'Vestimenta','5',null),
('Microfone Vedo - Youtuber', false, 'Eletrônico','4',null),
('Sofá retrátil', false, 'Móveis','3','3x57x80'),
('Farinha de arroz', false, 'Alimentos','2',null),
('Fire Stick Amazon', false, 'Eletrônico','3',null);

insert into orders(orderStatus, orderDescription, transportFee, paymentCash) values
( default, 'compra via aplicativo', null, true),
( default, 'compra via aplicativo', 50, true),
( 'Confirmado', null, null, true),
( default, 'compra via web site', 150, true),
( default, 'compra via aplicativo', null, true);

insert into productOrders (idProduct, idOrder, quantity, status) values
(1,5,2,null),
(2,5,1,null),
(3,6,1,null);

insert into productStorages (Address, quantity) values
('Rio de Janeiro',1000),
('Rio de Janeiro',500),
('São Paulo',10),
('São Paulo',100),
('São Paulo',10),
('Brasília',60);

insert into storageLocations (idProduct, idProductStorage, Address) values
(1,2,'RJ'),
(2,6,'GO');

INSERT INTO suppliers(socialName,CNPJ,contact) values
('Almeida e filhos',123456789123456,'21985474'),
('Eletrônicos Silva',84541964914357,'21985474'),
('Eletrônicos Valma',934567893934695,'21985474');

insert into productSupplier(idSupplier,idProduct, quantity) values
(1,1,500),
(1,2,400),
(2,4,633),
(3,3,5),
(2,5,10);

insert into sellers(socialName,AbstName,CNPJ,CPF,Address,contact) values 
('Tech eletronics', null, 123456789456321, null, 'Rio de Janeiro', 219946827),
('Boutique Durgas',null, null, 123456783, 'Rio de Janeiro', 219567895),
('Kids World', null, 456789123654485, null, 'São Paulo', 1198657484);

insert into productSeller(idSeller,idProduct,quantity) values
(1,6,80),
(2,7,10);

