import xmlrpc.client
import json

url = "https://ebramev-corporativo.odoo.com/"
db = "ebramev-corporativo"
username = 'marketing3@ebramev.com.br'
password = "31b97b66bcd98822b5ffd06c7a4ce5a34420b174"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Apenas registros ativos. Não os arquivados
CRM_Comercial = models.execute_kw(db, uid, password, 'crm.lead', 'search_read', [[['active', '=', True]]], {'fields': [
    'id',
    'display_name',
    'stage_id',
    'x_studio_interesse_principal',
    'expected_revenue',
    # Seller Info
    'create_uid',
    'user_id',
    # Contact Info
    'partner_id',
    'contact_name',
    'email_normalized',
    'phone',
    # Payment
    'x_studio_forma_de_pagamento',
    'x_studio_parcelamento',
    'x_studio_valor_p_parcela',
    'x_studio_dia_de_vencimento',
    ]}
)

print(json.dumps(CRM_Comercial, indent=2))
