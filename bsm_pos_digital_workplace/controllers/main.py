from odoo import fields, http, tools, _, exceptions
from odoo.http import request
from werkzeug.utils import redirect


class DwpWebsite(http.Controller):
    @http.route(['/'], type='http', auth="user", website=True)
    def home(self, **kw):
        
        return request.render("bsm_pos_digital_workplace.homefix")