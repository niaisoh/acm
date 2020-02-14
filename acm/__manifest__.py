# Copyright 2019 Ecosoft Co., Ltd (https://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

{
    'name': 'ACM :: Agreement Contract',
    'version': '12.0.1.0.0',
    'author': 'Ecosoft, Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'website': 'https://github.com/OCA/contract',
    'category': 'Agreement',
    'depends': [
        'agreement_legal',
        'contract',
        'report_qweb_element_page_visibility',
        'date_range',
        'excel_import_export',
        'web_timeline',
    ],
    'data': [
        # acm_agreement_contract
        'acm_agreement_contract/data/report_paperformat_data.xml',
        'acm_agreement_contract/data/report_data.xml',
        'acm_agreement_contract/data/agreement_subtype_data.xml',
        'acm_agreement_contract/data/agreement_data.xml',
        'acm_agreement_contract/data/breach_type_data.xml',
        'acm_agreement_contract/data/ir_cron.xml',
        'acm_agreement_contract/security/ir.model.access.csv',
        'acm_agreement_contract/wizards/agreement_create_wizards.xml',
        'acm_agreement_contract/wizards/agreement_extension_wizards.xml',
        'acm_agreement_contract/wizards/agreement_transfer_wizards.xml',
        'acm_agreement_contract/wizards/agreement_breach_wizards.xml',
        'acm_agreement_contract/wizards/agreement_terminate_wizards.xml',
        'acm_agreement_contract/wizards/agreement_create_contract_wizards.xml',
        'acm_agreement_contract/wizards/agreement_active_wizards.xml',
        'acm_agreement_contract/wizards/agreement_inactive_wizards.xml',
        'acm_agreement_contract/wizards/contract_create_invoice_wizards.xml',
        'acm_agreement_contract/wizards/contract_create_manual_invoice.xml',
        'acm_agreement_contract/wizards/contract_create_manual_rental_invoice.xml',
        'acm_agreement_contract/views/res_partner_views.xml',
        'acm_agreement_contract/views/res_company_views.xml',
        'acm_agreement_contract/views/product_views.xml',
        'acm_agreement_contract/views/account_views.xml',
        'acm_agreement_contract/views/goods_category_views.xml',
        'acm_agreement_contract/views/lock_attribute_views.xml',
        'acm_agreement_contract/views/account_analytic_account_views.xml',
        'acm_agreement_contract/views/agreement_views.xml',
        'acm_agreement_contract/views/acm_working_hours_views.xml',
        'acm_agreement_contract/views/acm_breach_type_views.xml',
        'acm_agreement_contract/views/account_payment_views.xml',
        'acm_agreement_contract/report/report_templates.xml',
        'acm_agreement_contract/report/report_agreement.xml',
        'acm_agreement_contract/report/report_appendix.xml',
        # acm_batch_invoice
        'acm_batch_invoice/data/batch_invoice_sequence.xml',
        'acm_batch_invoice/data/date_range.xml',
        'acm_batch_invoice/data/product.xml',
        'acm_batch_invoice/security/ir.model.access.csv',
        'acm_batch_invoice/wizard/acm_batch_invoice_wizard.xml',
        'acm_batch_invoice/views/account_invoice_views.xml',
        'acm_batch_invoice/views/acm_batch_invoice_views.xml',
        # Excel Import/Export
        'acm_batch_invoice/acm_batch_invoice_import_export/actions.xml',
        'acm_batch_invoice/acm_batch_invoice_import_export/templates.xml',
        # acm_reports
        'acm_reports/data/paper_format.xml',
        'acm_reports/security/ir.model.access.csv',
        'acm_reports/report/template/report_templates.xml',
        'acm_reports/report/report_templates.xml',
        'acm_reports/report/rental_collect_report.xml',
        'acm_reports/report/rental_analysis_report.xml',
        'acm_reports/report/report_voucher_acm.xml',
        'acm_reports/report/report_receipt_acm.xml',
        'acm_reports/report/report_receipt_tax_invoice_abb_acm.xml',
        'acm_reports/report/report_receipt_tax_invoice_acm.xml',
        'acm_reports/report/report_tax_invoice_abb_acm.xml',
        'acm_reports/report/report_multiday_receipt.xml',
        'acm_reports/report/report_multi_day_receipt.xml',
        'acm_reports/report/report.xml',
        'acm_reports/wizard/rental_collect_report_wizards.xml',
    ],
}
