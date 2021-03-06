# -*- coding: utf-8 -*-
#  <2016> <ToprpERP HeYang>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, api, fields, exceptions, _


class KjyPurchaseOrderPaymentType(models.Model):
    _name = 'kjy.purchase.order.payment.type'
    _description = u'付款类型'

    supplier_id = fields.Many2one('res.partner', string=u'供应商', index=True)
    name = fields.Char(string=u'类型名称')
    active = fields.Boolean(string=u'是否有效', default=True)

    _sql_constraints = [('payment_type_supplier_id_name_uniq', 'unique (supplier_id,name)', u'同一个供应商不可以设置相同的付款类型!'), ]
