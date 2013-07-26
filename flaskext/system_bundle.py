# -*- coding: utf-8 -*-
"""
    flaskext.system_bundle
    ~~~~~~~~~~~~~~~~~~~~~~

    Blueprints function in class, for programming with
    Bundle.

    :copyright: (c) 2013 by yograterol.
    :license: BSD, see LICENSE for more details.
"""
from yapsy.IPlugin import IPlugin
from yapsy.PluginManager import PluginManager
from flask import (Flask, Blueprint)


class Bundle(Blueprint, IPlugin):

    def __init__(self, *args, **kwargs):
        if not 'static_folder' in kwargs.keys():
            kwargs['static_folder'] = 'static'
        if not 'template_folder' in kwargs.keys():
            kwargs['template_folder'] = 'template'
        super(Bundle, self).__init__(*args, **kwargs)

    def register_blueprint(self, *args, **kwargs):
        super.register(*args, **kwargs)


class SystemBundle(object):

    __slots__ = ['app', 'debug', 'manager', 'name_folder_bundle',
                 'template_folder', 'static_folder']

    def __init__(self, name, debug=False, config_object=None,
                 name_folder_bundle='bundle', template_folder='template',
                 static_folder='static'):
        self.app = Flask(name)
        self.debug = debug
        self.app.config.from_object(config_object)
        self.name_folder_bundle = name_folder_bundle

    def create_manager(self):
        self.manager = PluginManager()
        self.manager.setPluginPlaces([self.name_folder_bundle,])
        self.manager.collectPlugins()

    def register_bundle(self):
        for bundle in self.manager.getAllPlugins():
            bundle.plugin_object.register_blueprint(self.app)

    def load_app(self):
        self.app.run(debug=self.debug)

