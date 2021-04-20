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


class CCTVSystem(models.Model):
    _name = "cctv.system"
    _description = "CCTV System"


    name = fields.Char(string='Camera Description', required=True)
    cctv_qty = fields.Integer(string='Qty',store=True)
    cctv_status = fields.Selection([('New', 'New'), ('Used', 'Used')],string='Status',default='New')
    is_camera = fields.Boolean('Is Camera?')
    cctv_check_clean = fields.Selection([('Cheeked', 'Cheeked'), ('Cleaned', 'Cleaned'),('Pasitien','Pasitien')], string='Cheeked/Cleaned')
    cctv_note = fields.Text(string='CCTV Note')
    day_cctv_vision = fields.Boolean('Day Vision')
    night_cctv_vision = fields.Boolean('Night Vision')
    # cctv_vision = fields.Selection([('Day Vision', 'Day Vision'), ('Night Vision', 'Night Vision'),('Night Vision', 'Night Vision')],string='Camera Vision',)
    from_date = fields.Datetime(string='From Date')
    upto_date = fields.Datetime(string="UP to Date")
    checklist_id = fields.Many2one('atm.checklist', string='ATM Checklist')


class CCTVSystemDescription(models.Model):
    _name = "cctv.system.description"
    _description = "CCTV System Description"


    name = fields.Char(string='Devices Description', required=True)
    cctvdes_qty = fields.Integer(string='Qty',store=True)
    cctvdes_status = fields.Selection([('New', 'New'), ('Used', 'Used')],string='Status',default='New')
    cctvdes_check_clean = fields.Selection([('Cheeked', 'Cheeked'), ('Cleaned', 'Cleaned'),('Pasitien','Pasitien')], string='Cheeked/Cleaned')
    cctvdes_note = fields.Text(string='CCTV Note')
    # cctv_vision = fields.Selection([('Day Vision', 'Day Vision'), ('Night Vision', 'Night Vision'),('Night Vision', 'Night Vision')],string='Camera Vision',)
    checklist_id = fields.Many2one('atm.checklist', string='ATM Checklist')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: