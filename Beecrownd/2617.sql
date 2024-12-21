select products.name,providers.name
from providers, products
where providers.id = products.id_providers and providers.name = 'Ajax SA';