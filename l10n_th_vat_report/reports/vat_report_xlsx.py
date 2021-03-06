# Copyright 2019 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

import logging
from odoo import models
_logger = logging.getLogger(__name__)


class ReportVatReportXlsx(models.TransientModel):
    _name = 'report.l10n_th_vat_report.report_vat_report_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def _get_ws_params(self, wb, data, objects):
        company_template = {
            '1_blank': {
                'header': {
                    'value': '',
                    'format': self.format_tcell_left,
                },
                'data': {
                    'value': '',
                },
                'width': 3,
            },
            '2_period': {
                'header': {
                    'value': 'Period',
                },
                'data': {
                    'value': self._render('period'),
                },
                'width': 12,
            },
            '3_partner': {
                'header': {
                    'value': 'Partner',
                },
                'data': {
                    'value': self._render('partner'),
                },
                'width': 18,
            },
            '4_tax_id': {
                'header': {
                    'value': 'Tax ID',
                },
                'data': {
                    'value': self._render('tax_id'),
                },
                'width': 30,
            },
            '5_branch_id': {
                'header': {
                    'value': 'Branch ID',
                },
                'data': {
                    'value': self._render('branch_id'),
                },
                'width': 15,
            },
        }
        vat_template = {
            '1_index': {
                'header': {
                    'value': '#',
                },
                'data': {
                    'value': self._render('row_pos'),
                },
                'width': 3,
            },
            '2_tax_date': {
                'header': {
                    'value': 'Date',
                },
                'data': {
                    'value': self._render('tax_date'),
                },
                'width': 12,
            },
            '3_tax_invoice': {
                'header': {
                    'value': 'Number',
                },
                'data': {
                    'value': self._render('tax_invoice'),
                },
                'width': 18,
            },
            '4_partner_name': {
                'header': {
                    'value': 'Cust./Sup.',
                },
                'data': {
                    'value': self._render('partner_name'),
                },
                'width': 30,
            },
            '5_partner_vat': {
                'header': {
                    'value': 'Tax ID',
                },
                'data': {
                    'value': self._render('partner_vat'),
                },
                'width': 15,
            },
            '6_partner_branch': {
                'header': {
                    'value': 'Branch ID',
                },
                'data': {
                    'value': self._render('partner_branch'),
                },
                'width': 12,
            },
            '7_tax_base_amount': {
                'header': {
                    'value': 'Base Amount',
                },
                'data': {
                    'value': self._render('tax_base_amount'),
                    'format': self.format_tcell_amount_right,
                },
                'width': 21,
            },
            '8_tax_amount': {
                'header': {
                    'value': 'Tax Amount',
                },
                'data': {
                    'value': self._render('tax_amount'),
                    'format': self.format_tcell_amount_right,
                },
                'width': 21,
            },
            '9_doc_ref': {
                'header': {
                    'value': 'Doc Ref.',
                },
                'data': {
                    'value': self._render('doc_ref'),
                },
                'width': 18,
            },
        }
        ws_params = {
            'ws_name': 'VAT Report',
            'generate_ws_method': '_vat_report',
            'title': 'VAT Report',
            'wanted_list_company': [k for k in sorted(company_template.keys())],
            'col_specs_company': company_template,
            'wanted_list': [k for k in sorted(vat_template.keys())],
            'col_specs': vat_template,
        }
        if objects.tax_id.type_tax_use == "sale":
            ws_params['ws_name'] = 'Sale VAT Report'
            ws_params['title'] = 'Sale VAT Report'
        elif objects.tax_id.type_tax_use == "purchase":
            ws_params['ws_name'] = 'Purchase VAT Report'
            ws_params['title'] = 'Purchase VAT Report'

        return [ws_params]

    def _vat_report(self, wb, ws, ws_params, data, objects):
        ws.set_portrait()
        ws.fit_to_pages(1, 0)
        ws.set_header(self.xls_headers['standard'])
        ws.set_footer(self.xls_footers['standard'])
        self._set_column_width(ws, ws_params)
        row_pos = 0
        # title
        row_pos = self._write_ws_title(ws, row_pos, ws_params, True)
        # company data
        row_pos = self._write_line(
            ws, row_pos, ws_params, col_specs_section='header',
            default_format=self.format_theader_blue_left,
            col_specs='col_specs_company', wanted_list='wanted_list_company')
        row_pos = self._write_line(
            ws, row_pos, ws_params, col_specs_section='data',
            render_space={
                'period': objects.date_range_id.display_name or '',
                'partner': objects.company_id.display_name or '',
                'tax_id': objects.company_id.partner_id.vat or '',
                'branch_id': objects.company_id.partner_id.branch or '',
            },
            default_format=self.format_tcell_left,
            col_specs='col_specs_company', wanted_list='wanted_list_company')
        row_pos += 1
        # vat report table
        row_pos = self._write_line(
            ws, row_pos, ws_params, col_specs_section='header',
            default_format=self.format_theader_blue_left,
            col_specs='col_specs', wanted_list='wanted_list')
        ws.freeze_panes(row_pos, 0)
        for obj in objects:
            total_base = 0.00
            total_tax = 0.00
            for line in obj.results:
                total_base += line.tax_base_amount
                total_tax += abs(line.tax_amount)
                row_pos = self._write_line(
                    ws, row_pos, ws_params, col_specs_section='data',
                    render_space={
                        'row_pos': row_pos-5,
                        'tax_date': line.tax_date or '',
                        'tax_invoice': line.tax_invoice or '',
                        'partner_name': line.partner_id.display_name or '',
                        'partner_vat': line.partner_id.vat or '',
                        'partner_branch': line.partner_id.branch or '',
                        'tax_base_amount': line.tax_base_amount or 0.00,
                        'tax_amount': abs(line.tax_amount) or 0.00,
                        'doc_ref': line.name or '',
                    },
                    default_format=self.format_tcell_left,
                    col_specs='col_specs', wanted_list='wanted_list')
        ws.write_row(row_pos, 6, [total_base, total_tax],
                     self.format_theader_blue_amount_right)
