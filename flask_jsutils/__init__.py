#!/usr/bin/env python
# -*- coding: utf-8 -*-

# based on https://github.com/dantezhu/flask_util_js/

__version__ = '0.1'

from flask import current_app, Response, Markup, Blueprint, url_for, render_template

class JSUtils(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)
        
    def init_app(self, app):
        self.blueprint = Blueprint("jsutils", __name__, template_folder='templates')

        url_prefix = app.config.get('JSUTILS_URL_PREFIX', '/jsutils')
        self.path = app.config.get('JSUTILS_SCRIPT_PATH', '/utils.js')

        @self.blueprint.route(self.path)
        def serve_js():
            return Response(
                self.content(),
                content_type='text/javascript; charset=UTF-8',
                headers={
                    'Cache-Control':'no-cache',
                }
            )

        @app.context_processor
        def inject_jsutils():
            return dict(jsutils=self)

        app.register_blueprint(self.blueprint, url_prefix=url_prefix)
        
    def content(self):
        rule_map = dict(
            [(r.endpoint, r.rule) for r in current_app.url_map._rules]
        )

        return render_template("utils.js", rule_map=rule_map)

    @property
    def js_link(self):
        return Markup('<script src="%s" type="text/javascript" charset="utf-8"></script>' % url_for("jsutils.serve_js"))

    @property
    def js_content(self):
        return Markup('<script type="text/javascript" charset="utf-8">%s</script>' % self.content())
