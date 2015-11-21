# -*- coding: utf-8 -*-

"""
Created on 2015-11-18
:author: markus (markus@terminal21.de)
"""

pytest_plugins = "kotti"

from pytest import fixture


@fixture(scope='session')
def custom_settings():
    import praxisloester.resources
    praxisloester.resources  # make pyflakes happy
    return {
        'kotti.configurators': 'kotti_tinymce.kotti_configure '
                               'praxisloester.kotti_configure'}
