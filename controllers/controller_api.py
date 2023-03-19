from server.odoo import http
from server.odoo.http import Controller, route, request
from server.odoo.tools import html_escape

class MyController(Controller):

    @http.route('/my_route', auth='public', type='http')
    def my_route(self, **kw):
        # Your controller logic here
        my_contacts = http.request.env['res.partner'].search([])
        outpute = ' '
        for contact in my_contacts:
            outpute += '<li>' + contact['name'] + '</li>'
        outpute += '<li/>'
        data = {'message': outpute}
        html_content = """
                <html>
                <head>
                    <title>Ma page HTML</title>
                </head>
                <body>
                    <h1>{}</h1>
                </body>
                </html>
                """.format(html_escape(data['message']))

        return html_content


