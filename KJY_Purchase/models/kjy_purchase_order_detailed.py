# -*- coding: utf-8 -*-
#  <2016> <ToprpERP HeYang>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, api, fields, exceptions, _


class KjyPurchaseOrderDetailed(models.Model):
    _name = 'kjy.purchase.order.detailed'
    _description = u'采购单明细'

    @api.multi
    @api.depends('originator_hr_id')
    def _get_product_info(self):
        for item in self:
            item.purchase_categories = item.originator_hr_id.type
            item.purchase_unit = item.originator_hr_id.uom_id.name

    purchase_order_id = fields.Many2one('kjy.purchase.order', string=u'采购单', index=True)
    originator_hr_id = fields.Many2one('product.product', string=u'采购产品', index=True)
    purchase_categories = fields.Char(string=u'产品类别', compute="_get_product_info", store=True)
    purchase_unit = fields.Char(string=u'产品单位', compute="_get_product_info", store=True)
    purchase_quantity = fields.Integer(string=u'采购数量', default=1)
    storage_quantity = fields.Integer(string=u'入库数量')
    faulty_quantity = fields.Integer(string=u'报损数量')
    remark = fields.Text(string=u'备注')

    @api.onchange('originator_hr_id')
    def onchange_originator_hr_id(self):
        if self.originator_hr_id:
            for item in self:
                item.purchase_categories = item.originator_hr_id.type
                item.purchase_unit = item.originator_hr_id.uom_id.name
