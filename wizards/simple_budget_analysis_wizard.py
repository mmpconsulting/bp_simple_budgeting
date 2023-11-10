from odoo import fields, models, api, _
from odoo.exceptions import UserError
import datetime
from calendar import monthrange
from pprint import pprint


class SimpleBudgetAnalysisWizard(models.TransientModel):
    _name = 'simple.budget.analysis.wizard'

    budget_plan_id = fields.Many2one('bp.simple.budget', string='Budget Plan')
    line_ids = fields.One2many(
        'budget.analysis.wizard.line', 'wizard_id', 'Lines')

    def action_submit(self):
        wizard_line = []
        month_fields = ['bg_jan', 'bg_feb', 'bg_mar', 'bg_apr', 'bg_may',
                        'bg_jun', 'bg_jul', 'bg_aug', 'bg_sep', 'bg_oct', 'bg_nov', 'bg_dec']
        monthnames = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni',
                      'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']

        for budget_line in self.budget_plan_id.line_ids:
            for i, month in enumerate(month_fields):

                date_from = datetime.datetime(
                    year=int(self.budget_plan_id.year_period), month=i+1, day=1).date()

                last_day_of_month = monthrange(date_from.year, date_from.month)
                date_to = datetime.datetime(year=int(
                    self.budget_plan_id.year_period), month=i+1, day=last_day_of_month[1]).date()

                account_move_lines = self.env['account.move.line'].search([
                    ('account_id', '=', budget_line.account_id.id),
                    ('date', '>=', date_from),
                    ('date', '<=', date_to),
                ])

                vals = {
                    'account_id': budget_line.account_id.id,
                    'monthname': monthnames[i],
                    'year': self.budget_plan_id.year_period,
                    'planned_amount': budget_line[month_fields[i]],
                    'practical_amount': sum(account_move_lines.mapped('balance')),
                }

                wizard_line.append([0, 0, vals])

        self.write({
            'line_ids': wizard_line
        })

        return {
            'name': ('Budget Analysis'),
            'type': 'ir.actions.act_window',
            'view_id': self.env.ref('bp_simple_budgeting.budget_analysis_wizard_line_tree').id,
            'view_mode': 'tree',
            'res_model': 'budget.analysis.wizard.line',
            'domain': [('wizard_id', '=', self.id)],
            'context': {'group_by': 'account_id'}
        }
