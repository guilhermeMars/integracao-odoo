import xmlrpc.client
import json

url = "https://ebramev-corporativo.odoo.com/"
db = "ebramev-corporativo"
username = 'marketing3@ebramev.com.br'
password = "31b97b66bcd98822b5ffd06c7a4ce5a34420b174"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

modulos = models.execute_kw(db, uid, password, 'x_modulos', 'search_read', [[['x_active', '=', True]]], {'fields': ['x_name', 'x_studio_curso', 'x_studio_ementa_prtica'], 'limit': 5})

print(json.dumps(modulos, indent=2))