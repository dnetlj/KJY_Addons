# -*- coding: utf-8 -*-
#  <2016> <ToprpERP HeYang>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, api, fields, exceptions, _


class KjyPurchaseOrder(models.Model):
    _name = 'kjy.purchase.order'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _description = u'采购单'
    _order = 'name desc'

    @api.multi
    @api.depends('name')
    def _compute_money(self):
        print 222233333444
        for item in self:
            pass

    name = fields.Char(string=u'采购单编号', default='/')
    supplier_id = fields.Many2one('res.partner', string=u'供应商', index=True)
    originator_hr_id = fields.Many2one('hr.employee', string=u'编制人', index=True,
                                       default=lambda self: self.env.uid)
    originator_company_id = fields.Many2one('res.company', string=u'编制公司', index=True,
                                            default=lambda self: self.env.user.company_id)
    purchase_amount = fields.Float(string=u'采购金额')
    other_payable_amount = fields.Float(string=u'其他应付金额')
    down_payments_amount = fields.Float(string=u'首付金额')
    unpaid_amount = fields.Float(string=u'未付金额', compute="_compute_money", store=True)
    paid_amount = fields.Float(string=u'已付金额', compute="_compute_money", store=True)
    state = fields.Selection(
        [('draft', u'草稿'), ('to_be_signed', u'待签合同'), ('down_payment', u'待付首付款'), ('to_be_shipped', u'待发货'),
         ('stay_in_port', u'待到港'), ('pending_delivery', u'待提货'), ('to_be_cleared', u'待清关'),
         ('to_be_in_storage', u'待入库'), ('end_of_payment', u'待付尾款'), ('stay_clean', u'待两清'),
         ('has_two', u'已两清')], string=u'状态', default='draft', track_visibility="onchange")
    warehousing_id = fields.Char(string=u'入库仓库')
    payment_type_id = fields.Many2one('kjy.purchase.order.payment.type', string=u'付款类型', index=True)
    detailed_ids = fields.One2many('kjy.purchase.order.detailed', 'purchase_order_id', string=u'采购明细')
    payment_id = fields.Many2one('kjy.purchase.order.payment', string=u'付款单')
    attachment_ids = fields.Many2many('ir.attachment', 'kjy_purchase_order_attchment_rel', 'zhu_id', 'fu_id',
                                      string=u"采购合同附件")

    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/':
            vals['name'] = self.env['ir.sequence'].get('kjy.purchase.order') or '/'

        obj = super(KjyPurchaseOrder, self).create(vals)
        return obj
