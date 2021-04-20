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


class BuglarAlarmSystem(models.Model):
    _name = "buglar.alarm.system"
    _description = "Buglar Alarm System"


    name = fields.Char(string='Devices Description', required=True)
    alarm_qty = fields.Integer(string='Qty',store=True)
    alarm_status = fields.Selection([('New', 'New'), ('Used', 'Used')],string='Status',default='New')
    alarm_check_clean = fields.Selection([('Cheeked', 'Cheeked'), ('Cleaned', 'Cleaned')],string='Cheeked/Cleaned')
    alarm_note = fields.Text(string='Alarm Note')
    checklist_id = fields.Many2one('atm.checklist', string='ATM Checklist')




# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: