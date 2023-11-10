from calendar import monthrange
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from pprint import pprint
import datetime


class SimpleBudget(models.Model):
    _name = 'bp.simple.budget'

    name = fields.Char(string='Name')
    date_select = fields.Date(string='Date/Year Select')
    year_period = fields.Char(
        string='Year', compute='_compute_year_periode', store=True)
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date From')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('posted', 'Post'),
    ], string='Status', default='draft')
    company_id = fields.Many2one(
        comodel_name='res.company', string='Company', default=lambda x: x.env.user.company_id.id)
    line_ids = fields.One2many(
        comodel_name='bp.simple.budget.line',
        inverse_name='budget_id',
        string='Budget Lines',
    )

    @api.depends('date_select')
    def _compute_year_periode(self):
        for record in self:
            if record.date_select:
                record.year_period = record.date_select.strftime("%Y")

                first_date = datetime.datetime(
                    year=self.date_select.year, month=1, day=1)
                last_date = datetime.datetime(
                    year=self.date_select.year, month=12, day=31)

                self.date_from = first_date.date()
                self.date_to = last_date.date()

    def action_confirm(self):
        self.write({
            'state': 'posted'
        })

    def action_cancel(self):
        self.write({
            'state': 'draft'
        })

    @api.multi
    def unlink(self):
        for record in self:
            if record.state not in ('draft'):
                raise UserError(
                    'You cannot delete a document which is not draft!'
                )
        return super(SimpleBudget, self).unlink()
