# -*- coding: utf-8 -*-
"""
    flaskext.system_bundle
    ~~~~~~~~~~~~~~~~~~~~~~

    Blueprints function in class, for programming with
    Bundle.

    :copyright: (c) 2013 by yograterol.
    :license: BSD, see LICENSE for more details.
"""
from distutils.sysconfig import get_python_lib
from os.path import join as joinpath
from os import (listdir, exists, isdir, splitext)
from imp import (find_module, load_module)
from flask import Flask


class SystemBundle(object):

    __slots__ = ['app', 'debug', 'bundle_namespace', 'test']

    def __init__(self, name, debug=False, config_object=None,
                 bundle_namespace='bundle', test=False):
        self.app = Flask(name)
        self.debug = debug
        self.app.config.from_object(config_object)
        if isdir(bundle_namespace):
            self.bundle_namespace = bundle_namespace
        else:
            self.bundle_namespace = joinpath(get_python_lib(), bundle_namespace)
        self.test = test

    def load_module(self):
        init = '__init__.py'
        bundles_list = listdir(self.bundle_namespace)
        bundles = dict()

        for bundle_name in bundles_list:
            f, filename, descr = find_module(bundle_name, [self.bundle_namespace])
            if isdir(joinpath(self.bundle_namespace, bundle_name)) and \
                exists(joinpath(self.bundle_namespace, bundle_name, init)):
                bundles[bundle_name] = load_module(bundle_name, f, filename, descr)
            name, extension = splitext(bundle_name)
            if extension == '.py' and not name == init:
                bundles[bundle_name] = load_module(bundle_name, f, filename, descr)
        self.register_blueprint(bundles)

    def register_blueprint(self, bundles_list):
        for bundle in bundles_list.iteritems():
            self.app.register_blueprint(getattr(bundle, 'bundle'))

    def load_app(self):
        if self.test:
            self.app.config['TESTING'] = True
            return self.app.test_client()
        self.app.run(debug=self.debug)

