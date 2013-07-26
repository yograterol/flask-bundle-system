"""
flask-system-bundle
-------------------



Links
`````

* `documentation <http://packages.python.org/flask-system-bundle>`_
* `development version
  <http://github.com/USERNAME/REPOSITORY/zipball/master#egg=flask-system-bundle-dev>`_

"""
from setuptools import setup


setup(
    name='flask-system-bundle',
    version='0.1',
    url='',
    license='BSD',
    author='yograterol',
    author_email='yograterol@fedoraproject.org',
    description='Flask extension for work with bundles',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
