# -*- coding: utf-8 -*-
#################################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################
{
    'name': "Field Service Checklist",
    'summary': """
        This module is give you all information ATM Preventive Maintenance""",
    'description': """
        This module is give you all information ATM Preventive Maintenance
    """,
    'author': 'Acespritech Solutions Pvt. Ltd.',
    'website': 'http://www.acespritech.com',
    'category': 'Field Service',
    'version': '14.0.1.0.0',
    'sequence': 1,

    'depends': ['base','industry_fsm'],

    'data': [
        'security/atm_security.xml',
        'security/ir.model.access.csv',
        'demo/paper_formate_data.xml',
        'views/atm_checklist_sign.xml',
        'views/checklist.xml',
        'views/buglar_alarm_system.xml',
        'views/cctv_system.xml',
        'views/general_information.xml',
        'views/report_view.xml',
        'reports/atm_maintenance_report.xml',
        'reports/atm_maintenance_report_fieldservice.xml',
    ],
    'demo': ["demo/demo.xml"],
    'qweb': ['static/src/xml/atm_checklist_sign.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: