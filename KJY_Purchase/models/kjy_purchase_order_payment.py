# -*- coding: utf-8 -*-
#  <2016> <ToprpERP HeYang>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, api, fields, exceptions, _


class KjyPurchaseOrderPayment(models.Model):
    _name = 'kjy.purchase.order.payment'
    _description = u'采购单付款单'

    # purchase_order_id = fields.Many2one('kjy.purchase.order', string=u'采购单', index=True)
    name = fields.Char(string=u'付款单编号', default='/')
    cashier_partner_id = fields.Many2one('res.partner', string=u'收款单位', index=True)
    expense_type = fields.Char(string=u'费用类型')
    expense_amount = fields.Float(string=u'费用金额')
    apply_data = fields.Date(string=u'申请日期')
    applicant_id = fields.Many2one('hr.employee', string=u'申请人', index=True)
    invoice_no = fields.Char(string=u'发票号')
    invoice_test_data = fields.Date(string=u'发票核验日期')
    invoice_type = fields.Char(string=u'发票类型')
    invoice_amount = fields.Float(string=u'发票金额')
    invoice_inspection_man = fields.Many2one('hr.employee', string=u'发票检验人', index=True)
    payment_date = fields.Date(string=u'付款日期')
    payment_amount = fields.Float(string=u'付款金额')
    drawee_id = fields.Many2one('hr.employee', string=u'付款人', index=True)
    relate_document_type = fields.Char(string=u'相关单据类型')
    relevant_document_number = fields.Char(string=u'相关单据号')
    state = fields.Selection(
        [('draft', u'草稿'), ('pending_payment', u'待付款'), ('already_paid', u'已付款'), ('has_refused', u'已拒绝')],
        string=u'状态', default='draft')

    # from_pay_order
