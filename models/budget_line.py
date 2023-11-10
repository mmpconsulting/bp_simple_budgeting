from odoo import models, fields, api


class SimpleBudgetLine(models.Model):
    _name = 'bp.simple.budget.line'

    budget_id = fields.Many2one(
        comodel_name='bp.simple.budget',
        string='Budget'
    )
    account_id = fields.Many2one('account.account', string='Account', required=True, domain=[
                                 ('deprecated', '=', False), ('user_type_id.type', '!=', 'view')], )
    name = fields.Char(string='Label')
    currency_id = fields.Many2one('res.currency', 'Currency', required=True,
                                  default=lambda self: self.env.user.company_id.currency_id.id)
    bg_jan = fields.Float(string='January')
    bg_feb = fields.Float(string='February')
    bg_mar = fields.Float(string='March')
    bg_apr = fields.Float(string='April')
    bg_may = fields.Float(string='May')
    bg_jun = fields.Float(string='June')
    bg_jul = fields.Float(string='July')
    bg_aug = fields.Float(string='August')
    bg_sep = fields.Float(string='September')
    bg_oct = fields.Float(string='October')
    bg_nov = fields.Float(string='November')
    bg_dec = fields.Float(string='December')

    annual_amount = fields.Float(
        compute='_compute_total', string='Annual Total', store=True)

    @api.depends('bg_jan', 'bg_feb', 'bg_mar', 'bg_apr', 'bg_may', 'bg_jun', 'bg_jul', 'bg_aug', 'bg_sep', 'bg_oct', 'bg_nov', 'bg_dec')
    def _compute_total(self):
        for rec in self:
            rec.annual_amount = rec.bg_jan + rec.bg_feb + rec.bg_mar + rec.bg_apr + rec.bg_may + \
                rec.bg_jun + rec.bg_jul + rec.bg_aug + \
                rec.bg_sep + rec.bg_oct + rec.bg_nov + rec.bg_dec
