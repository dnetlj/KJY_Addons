# -*- coding: utf-8 -*-
# © <2016> <TopOdoo Pengyb>

from odoo import fields, models, api, _
from odoo.exceptions import Warning


class ResPartner(models.Model):
    _inherit = "res.partner"

    e_business_license_no = fields.Char(string=u'营业执照或企业信用代码', size=20)
    e_business_license_img = fields.Binary(string=u'营业执照图片')
    p_card_no = fields.Char(string=u'身份证编号')
    p_card_img = fields.Binary(string=u'身份证图片')

    client_level = fields.Selection([('A','A'),('B','B'),('C','C'),('D','D')],string=u'客户等级')

    supplier_credit_limit = fields.Float(string=u'供应商信用额度',default=0.0)
    supplier_credit_limit_available = fields.Float(string=u'供应商信用额度', default=0.0)

    @api.multi
    def revert_supplier_credit_available(self,credit_limit,related_no=None,related_type=None):
        '''
        恢复供应商可用信用额度
        :param credit_limit:
        :param related_no:
        :param related_type:
        :return:
        '''
        self
        if credit_limit > self.supplier_credit_limit_available:
            self.supplier_credit_limit_available += credit_limit
            if self.supplier_credit_limit_available > self.supplier_credit_limit:
                self.supplier_credit_limit_available = self.supplier_credit_limit
            return True

    @api.multi
    def deduction_supplier_credit_available(self, credit_limit, related_no=None, related_type=None):
        '''
        扣除供应商可用信用额度
        :param credit_limit:
        :param related_no:
        :param related_type:
        :return:
        '''
        if credit_limit >= self.supplier_credit_limit_available:
            self.supplier_credit_limit_available -= credit_limit
            return True
        else:
            raise Warning(_(u'该供应商信用额度不足,目前可用额度: %s' % self.supplier_credit_limit_available))

