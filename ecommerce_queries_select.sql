 select * from clients c, orders o where c.idClient = o.idClient;

select concat (fname,' ', lname) as client, idOrder as request, orderStatus as status from clients c, orders o where c.idClient = o.idClient;

select * from clients c
inner join orders o on c.idClient = o.idOrder
inner join productOrders po on po.idOrder = o.idOrder;

select c.idClient, Fname, count(*) as Number_of_orders from clients c
inner join orders o on c.idClient = o.idClient
GROUP BY idClient;