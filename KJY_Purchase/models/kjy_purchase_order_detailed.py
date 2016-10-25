# -*- coding: utf-8 -*-
#  <2016> <ToprpERP HeYang>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, api, fields, exceptions, _


class KjyPurchaseOrderDetailed(models.Model):
    _name = 'kjy.purchase.order.detailed'
    _description = u'采购单明细'

    purchase_order_id = fields.Many2one('kjy.purchase.order', string=u'采购单', index=True)
    originator_hr_id = fields.Many2one('product.product', string=u'采购产品', index=True)
    purchase_categories = fields.Char(string=u'采购类别')
    purchase_unit = fields.Char(string=u'采购单位')
    purchase_quantity = fields.Integer(string=u'采购数量')
    storage_quantity = fields.Integer(string=u'入库数量')
    faulty_quantity = fields.Integer(string=u'报损数量')
    remark = fields.Text(string=u'备注')