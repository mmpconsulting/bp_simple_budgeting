# -*- coding: utf-8 -*-
from odoo import http

# class BpSimpleBudgeting(http.Controller):
#     @http.route('/bp_simple_budgeting/bp_simple_budgeting/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bp_simple_budgeting/bp_simple_budgeting/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bp_simple_budgeting.listing', {
#             'root': '/bp_simple_budgeting/bp_simple_budgeting',
#             'objects': http.request.env['bp_simple_budgeting.bp_simple_budgeting'].search([]),
#         })

#     @http.route('/bp_simple_budgeting/bp_simple_budgeting/objects/<model("bp_simple_budgeting.bp_simple_budgeting"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bp_simple_budgeting.object', {
#             'object': obj
#         })