"""
Flask-JSUtils
---------------

Flask-JSUtils allows you to use methods such as url_for() in your javascript.

"""
import re
from setuptools import setup


def run_tests():
    from tests import suite
    return suite()


setup(
    name='Flask-JSUtils',
    version='0.1',
    license='BSD',
    author='Semion Sidorenko',
    author_email='semion'+'.'+'sidorenko@gmail.com',
    url='http://github.com/ssidorenko/flask-jsutils',
    description='Flask utilities in your javascript',
    long_description=__doc__,
    packages=['flask_jsutils'],
    zip_safe=False,
    platforms='any',
    install_requires=['Flask>=0.10'],
    test_suite='__main__.run_tests',
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
