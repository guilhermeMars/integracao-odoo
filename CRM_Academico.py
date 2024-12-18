import xmlrpc.client
import json

url = "https://ebramev-corporativo.odoo.com/"
db = "ebramev-corporativo"
username = 'marketing3@ebramev.com.br'
password = "31b97b66bcd98822b5ffd06c7a4ce5a34420b174"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

CRM_Academico = models.execute_kw(db, uid, password, 'x_academico', 'search_read', [[['x_active', '=', True]]], {'fields': [
    'id',
    'create_date',
    'x_studio_stage_id',
    'create_uid',
    'x_name',
    'x_studio_partner_id',
    'x_studio_partner_email',
    'x_studio_partner_phone',
    ]}
)

print(json.dumps(CRM_Academico, indent=2))
