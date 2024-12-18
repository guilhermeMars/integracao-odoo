import xmlrpc.client
import json

url = "https://ebramev-corporativo.odoo.com/"
db = "ebramev-corporativo"
username = 'marketing3@ebramev.com.br'
password = "31b97b66bcd98822b5ffd06c7a4ce5a34420b174"

## "Meta-calls which don’t require authentication, such as the authentication itself or fetching version information"
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())
uid = common.authenticate(db, username, password, {})
print(uid)

## execute_kw: pode ser utilizado para executar funções de um modelo em específíco

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

## Ids e Leitura separados
# modulos_id = models.execute_kw(db, uid, password, 'x_modulos', 'search', [[['x_active', '=', True]]])
# modulos = models.execute_kw(db, uid, password, 'x_modulos', 'read', [modulos_id], {'fields': ['x_name', 'x_studio_curso', 'x_studio_ementa_prtica']})

## Ids e Leitura juntas
modulos = models.execute_kw(db, uid, password, 'x_modulos', 'search_read', [[['x_active', '=', True]]], {'fields': ['x_name', 'x_studio_curso', 'x_studio_ementa_prtica'], 'limit': 5})

print(json.dumps(modulos, indent=2))

