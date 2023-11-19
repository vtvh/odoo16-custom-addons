# -*- coding: utf-8 -*-
# from odoo import http


# class Poolplayer(http.Controller):
#     @http.route('/poolplayer/poolplayer', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/poolplayer/poolplayer/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('poolplayer.listing', {
#             'root': '/poolplayer/poolplayer',
#             'objects': http.request.env['poolplayer.poolplayer'].search([]),
#         })

#     @http.route('/poolplayer/poolplayer/objects/<model("poolplayer.poolplayer"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('poolplayer.object', {
#             'object': obj
#         })
