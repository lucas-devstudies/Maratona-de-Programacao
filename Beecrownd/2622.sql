select c.name
from customers as c
inner join legal_person as l
on l.id_customers = c.id