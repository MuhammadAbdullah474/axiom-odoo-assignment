# -*- coding: utf-8 -*-
# from odoo import http


# class My-test-module(http.Controller):
#     @http.route('/my-test-module/my-test-module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my-test-module/my-test-module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my-test-module.listing', {
#             'root': '/my-test-module/my-test-module',
#             'objects': http.request.env['my-test-module.my-test-module'].search([]),
#         })

#     @http.route('/my-test-module/my-test-module/objects/<model("my-test-module.my-test-module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my-test-module.object', {
#             'object': obj
#         })
