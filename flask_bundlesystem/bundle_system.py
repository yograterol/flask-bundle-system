# -*- coding: utf-8 -*-
"""
    flask_bundlesystem
    ~~~~~~~~~~~~~~~~~~~~~~

    Blueprints function in class, for programming with
    Blueprints as Bundles.

    :copyright: (c) 2013 by yograterol.
    :license: BSD, see LICENSE for more details.
"""
from os.path import (isdir, isfile, splitext, join)
from os import listdir
from imp import (find_module, load_module)
from flask import current_app


class BundleSystem(object):

    __slots__ = ['namespace_bundle', 'bundle_var_name']

    def __init__(self, namespace_bundle=None, bundle_var_name='bundle'):
        self.namespace_bundle = namespace_bundle
        self.bundle_var_name = bundle_var_name
        if isdir(namespace_bundle):
            self.namespace_bundle = namespace_bundle
        else:
            raise Exception("The namespace_bundle value is not a valid path.")
        self.load_module()

    def register_bundle(self, bundles_dict):
        """
        Get the variables bundle and register in the Flask App.
        :params:
            bundles_dict - Dictionary with all bundles (Blueprints)
        """
        for bundle_name, bundle in bundles_dict.iteritems():
            # Try get bundle variable and bundle_config variable
            blueprint = getattr(bundle, self.bundle_var_name, None)
            kwargs = getattr(bundle, self.bundle_var_name + '_config',
                             dict())
            if blueprint:
                # Register the blueprint
                current_app.register_blueprint(blueprint, **kwargs)

    def load_module(self, folder=None):
        """
        Method recursive
        Find all files in the current project path, and try import the bundle
        name.
        :params:
            folder - The absolute path of the folder to find.
        """
        if not folder:
            folder = self.namespace_bundle

        bundles_list_dir = listdir(folder)
        bundles = dict()

        for bundle_name in bundles_list_dir:
            # Join the path folder and bundle name file for check if is folder
            # or file.
            abs_path = join(folder, bundle_name)
            if isdir(abs_path):
                self.load_module(abs_path)

            if isfile(abs_path):
                try:
                    # Split the bundle name, for only check python files.
                    name, extension = splitext(bundle_name)
                    if extension == '.py':
                        f, filename, descr = find_module(name, [folder, ])
                        bundles[bundle_name] = load_module(name, f,
                                                           filename, descr)
                except ImportError:
                    continue
        # After of check all bundles name in the current "folder", passing
        # bundles dict as parameter to method register_bundle.
        self.register_bundle(bundles)
