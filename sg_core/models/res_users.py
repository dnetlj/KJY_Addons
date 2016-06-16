# -*- coding: utf-8 -*-

from openerp import models, fields, api


class ResDepartment(models.Model):
    _name = 'res.department'

    name = fields.Char(string=u'Name', required=True)
    company_id = fields.Many2one('res.company', string=u'Company', required=True)
    parent_id = fields.Many2one('res.department', string=u'Parent Department')


class ResJob(models.Model):
    _name = 'res.job'

    name = fields.Char(string=u'Name', required=True)
    company_id = fields.Many2one('res.company', string=u'Company', required=True)
    department_id = fields.Many2one('res.department', string=u'Department')


class ResUsers(models.Model):
    _inherit = 'res.users'

    department_id = fields.Many2one('res.department', string=u'Department')
    job_id = fields.Many2one('res.job', string=u'Job')
    mobile = fields.Char('Mobile', required=True)
    phone = fields.Char('Phone')
    fax = fields.Char('Fax')
