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


class GeneralInformation(models.Model):
    _name = "general.information"
    _description = "General Information"


    name = fields.Char(string='Devices Description', required=True)
    general_info_qty = fields.Integer(string='Qty',store=True)
    general_info_status = fields.Selection([('New', 'New'), ('Used', 'Used')],string='Status',default='New')
    general_info_check_clean = fields.Selection([('Cheeked', 'Cheeked'), ('Cleaned', 'Cleaned')], string='Cheeked/Cleaned')
    general_info_note = fields.Text(string='Alarm Note')
    checklist_id = fields.Many2one('atm.checklist', string='ATM Checklist')

    # time_diff_of_atm = fields.Char(string='Time Different of ATM:')
    # burglar_software = fields.Char(string='Burglar Software:')
    # status_of_ac_system = fields.Char(string='Status of A/C System:')
    # atm_machine_ip_address = fields.Char(string='ATM Machine IP Address:')
    # burglar_alarm_ip_address = fields.Char(string='Burglar Alarm IP Address:')
    # cctv_system_ip_address = fields.Char(string='CCTV System IP Address:')
    # coordinates_north = fields.Char(string='Coordinates North:')
    # to_dvr = fields.Char(string='to DVR :')
    # cctv_software = fields.Char(string='CCTV Software:')
    # room_temp = fields.Char(string='Room Temperature:')
    # type_of_machine = fields.Char(string='Type of Machine:')
    # clock_battery_of_sicep_mobo = fields.Char(string='Clock Battery of Sicep MOBO:')
    # status_of_glass_cover_camera = fields.Char(string='Status of Glass Cover Camera # 1:')
    # status_of_transaction_link = fields.Char(string='Status of Transaction Link:')
    # status_of_burglar_link = fields.Char(string='Status of Burglar Link:')
    # status_of_cctv_link = fields.Char(string='Status of CCTV Link:')
    # coordivates_east = fields.Char(string='Coordinates East:')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: