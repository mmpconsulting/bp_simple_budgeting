from odoo import fields, models, api, _
from odoo.exceptions import UserError


class BudgetAnalysisWizardLine(models.TransientModel):
    _name = 'budget.analysis.wizard.line'

    wizard_id = fields.Many2one(
        'simple.budget.analysis.wizard', 'Wizard', ondelete='cascade')
    account_id = fields.Many2one('account.account', string='Account')
    monthname = fields.Char(string='Month')
    year = fields.Char(string='Year')
    planned_amount = fields.Float(string='Planned Amount')
    practical_amount = fields.Float(string='Practical Amount')
    achievment = fields.Float(
        string='Achievment', compute='_compute_achivement',)

    @api.depends('planned_amount', 'practical_amount')
    def _compute_achivement(self):
        for rec in self:
            if rec.practical_amount and rec.planned_amount:
                rec.achievment = 100 * rec.practical_amount / rec.planned_amount
            else:
                rec.achievment = 0.0
