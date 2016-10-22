# -*- coding: utf-8 -*-
from odoo.exceptions import AccessError
from odoo.tests.common import TransactionCase


class TestRules(TransactionCase):
    """ This class extends the base TransactionCase, in order to test the
    accounting with localization setups. It is configured to run the tests after
    the installation of all modules, and will SKIP TESTS ifit  cannot find an already
    configured accounting (which means no localization module has been installed).
    """

    post_install = True
    at_install = False

    def setUp(self):
        super(TestRules, self).setUp()

        self.supplier = self.env['res.partner'].create({
            'name': 'Test Supplier',
            'is_supplier': True,
            'supplier_credit_limit': 1000000.0,
            'supplier_credit_limit_available': 1000000.0
        })

    def test_supplier_credit(self):
        """供应商的信用额度的测试"""

        if self.supplier:
            self.assertEqual(self.supplier.supplier_credit_limit_available, 1000000.0)
            self.assertEqual(self.supplier.supplier_credit_limit, 1000000.0)

            # 扣除额度测试
            self.supplier.deduction_supplier_credit_available(20000.0)
            self.assertEqual(self.supplier.supplier_credit_limit_available, 980000.0)

            # 恢复额度测试
            self.supplier.revert_supplier_credit_available(10000)
            self.assertEqual(self.supplier.supplier_credit_limit_available, 990000.0)

            # 恢复额度测试（超额度限制）
            self.supplier.revert_supplier_credit_available(20000)
            self.assertEqual(self.supplier.supplier_credit_limit_available, 1000000.0)
