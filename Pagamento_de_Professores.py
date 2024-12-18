import xmlrpc.client
import json

url = "https://ebramev-corporativo.odoo.com/"
db = "ebramev-corporativo"
username = 'marketing3@ebramev.com.br'
password = "31b97b66bcd98822b5ffd06c7a4ce5a34420b174"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

Pagamento_Professores = models.execute_kw(db, uid, password, 'x_pagamento_de_profess', 'search_read', [[['x_active', '=', True]]], {'fields': [
    'id',
    'x_name',
    'create_date',
    'x_studio_input_de_pagamentos_realizado',
    'x_studio_stage_id',
    'x_studio_turma',
    'x_studio_reembolso',
    'x_studio_dados_bancrios', # (Pix)
    'x_studio_valor_do_reembolso',
    'x_studio_value', # (Prolabore)
    'x_studio_vencimento',
    'x_studio_quantos_p_vencer', # (Quantos dias para vencer)
    'x_studio_tipo',
    'x_studio_emisso_de_nf',
    ]}
)

print(json.dumps(Pagamento_Professores, indent=2))
