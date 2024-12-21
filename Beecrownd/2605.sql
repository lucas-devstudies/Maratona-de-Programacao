select p.name,f.name 
from products as p
inner join providers as f
On p.id_providers = f.id
inner join categories as c
on c.id = p.id_categories
where c.id = 6