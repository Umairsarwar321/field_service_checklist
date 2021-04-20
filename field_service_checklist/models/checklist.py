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
from odoo import fields, models
# from odoo.exceptions import ValidationError


class ATMChecklist(models.Model):
    _name = "atm.checklist"
    _description = "ATM Checklist"


    name = fields.Char(string='ATM Name', required=True)
    atm_code_no = fields.Integer(string='ATM Code No.',store=True)
    partner_id = fields.Many2one('res.partner', string='Customer',ondelete='restrict')
    city = fields.Char(related='partner_id.city',string='City', readonly=False)

    buglar_alarm_line = fields.One2many('buglar.alarm.system', 'checklist_id', string='Buglar Alarm Line',copy=True,auto_join=True)
    cctv_system_line = fields.One2many('cctv.system', 'checklist_id', string='CCTV System Line', copy=True,
                                        auto_join=True)
    cctvdes_system_line = fields.One2many('cctv.system.description', 'checklist_id', string='CCTV System Description Line', copy=True,
                                       auto_join=True)
    general_info_line = fields.One2many('general.information', 'checklist_id', string='General Information Line', copy=True,
                                        auto_join=True)
    from_date = fields.Datetime(string='From Date')
    upto_date = fields.Datetime(string="UP to Date")
    company_id = fields.Many2one('res.company', string='Company')

    signature = fields.Binary("Signature", readonly=True)

    time_diff_of_atm = fields.Char(string='Time Different of ATM:')
    burglar_software = fields.Char(string='Burglar Software:')
    status_of_ac_system = fields.Char(string='Status of A/C System:')
    atm_machine_ip_address = fields.Char(string='ATM Machine IP Address:')
    burglar_alarm_ip_address = fields.Char(string='Burglar Alarm IP Address:')
    cctv_system_ip_address = fields.Char(string='CCTV System IP Address:')
    coordinates_north = fields.Char(string='Coordinates North:')
    to_dvr = fields.Char(string='to DVR :')
    cctv_software = fields.Char(string='CCTV Software:')
    room_temp = fields.Char(string='Room Temperature:')

    type_of_machine = fields.Char(string='Type of Machine:')
    clock_battery_of_sicep_mobo = fields.Char(string='Clock Battery of Sicep MOBO:')
    status_of_glass_cover_camera = fields.Char(string='Status of Glass Cover Camera # 1:')
    status_of_transaction_link = fields.Char(string='Status of Transaction Link:')
    status_of_burglar_link = fields.Char(string='Status of Burglar Link:')
    status_of_cctv_link = fields.Char(string='Status of CCTV Link:')
    coordivates_east = fields.Char(string='Coordinates East:')

class ProjectTask(models.Model):
    _inherit = "project.task"
    _description = "Project Task"

    atm_checklist_id = fields.Many2one("atm.checklist", string='ATM Checklist')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: