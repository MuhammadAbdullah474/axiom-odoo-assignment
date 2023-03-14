# -*- coding: utf-8 -*-
# from odoo import http


# class AxiomAssignment(http.Controller):
#     @http.route('/axiom_assignment/axiom_assignment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/axiom_assignment/axiom_assignment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('axiom_assignment.listing', {
#             'root': '/axiom_assignment/axiom_assignment',
#             'objects': http.request.env['axiom_assignment.axiom_assignment'].search([]),
#         })

#     @http.route('/axiom_assignment/axiom_assignment/objects/<model("axiom_assignment.axiom_assignment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('axiom_assignment.object', {
#             'object': obj
#         })
