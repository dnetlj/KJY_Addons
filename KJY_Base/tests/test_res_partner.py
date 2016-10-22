# -*- coding: utf-8 -*-
from odoo.tests.common import HttpCase
from odoo.exceptions import ValidationError

class ResPartnerTestCase(HttpCase):
    """ This class extends the base TransactionCase, in order to test the
    accounting with localization setups. It is configured to run the tests after
    the installation of all modules, and will SKIP TESTS ifit  cannot find an already
    configured accounting (which means no localization module has been installed).
    """

    post_install = True
    at_install = False

    def setUp(self):
        pass

    def test_supplier_invoice(self):
        supplier = self.env['res.partner'].create({
            'name': 'Test Supplier',
            'is_supplier': True,
            'supplier_credit_limit': 1000000,
            'supplier_credit_limit_available': 1000000,
        })

        # 扣除额度测试
        supplier.deduction_supplier_credit_available(20000)
        self.assertTrue(supplier.supplier_credit_limit_available == 980000)

        # 恢复额度测试
        supplier.revert_supplier_credit_available(10000)
        self.assertTrue(supplier.supplier_credit_limit_available == 990000)

        # 恢复额度测试（超额度限制）
        supplier.revert_supplier_credit_available(20000)
        self.assertTrue(supplier.supplier_credit_limit_available == 1000000)


        analytic_account = self.env['account.analytic.account'].create({
            'name': 'test account',
        })

        # Should be changed by automatic on_change later
        invoice_account = self.env['account.account'].search([('user_type_id', '=', self.env.ref('account.data_account_type_receivable').id)], limit=1).id
        invoice_line_account = self.env['account.account'].search([('user_type_id', '=', self.env.ref('account.data_account_type_expenses').id)], limit=1).id

        invoice = self.env['account.invoice'].create({'partner_id': self.env.ref('base.res_partner_2').id,
            'account_id': invoice_account,
            'type': 'in_invoice',
        })

        self.env['account.invoice.line'].create({'product_id': self.env.ref('product.product_product_4').id,
            'quantity': 1.0,
            'price_unit': 100.0,
            'invoice_id': invoice.id,
            'name': 'product that cost 100',
            'account_id': invoice_line_account,
            'invoice_line_tax_ids': [(6, 0, [tax.id])],
            'account_analytic_id': analytic_account.id,
        })

        # check that Initially supplier bill state is "Draft"
        self.assertTrue((invoice.state == 'draft'), "Initially vendor bill state is Draft")

        #change the state of invoice to open by clicking Validate button
        invoice.action_invoice_open()

        #I cancel the account move which is in posted state and verifies that it gives warning message
        with self.assertRaises(Warning):
            invoice.move_id.button_cancel()