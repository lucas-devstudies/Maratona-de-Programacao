select m.id, m.name
from movies as m
inner join prices as p
on p.id = m.id_prices
where p.value < 2.00