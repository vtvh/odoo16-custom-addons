# -*- coding: utf-8 -*-
from odoo import http


class MyModlue(http.Controller):
    @http.route('/my_modlue/my_modlue', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/my_modlue/my_modlue/objects', auth='public')
    def list(self, **kw):
        return http.request.render('my_modlue.listing', {
            'root': '/my_modlue/my_modlue',
            'objects': http.request.env['my_modlue.my_modlue'].search([]),
        })

    @http.route('/my_modlue/my_modlue/objects/<model("my_modlue.my_modlue"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('my_modlue.object', {
            'object': obj
        })
