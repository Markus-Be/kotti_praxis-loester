# -*- coding: utf-8 -*-

"""
Created on 2015-11-18
:author: markus (markus@terminal21.de)
"""

from kotti.resources import File
from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('praxisloester')


def kotti_configure(settings):
    """ Add a line like this to you .ini file::

            kotti.configurators =
                praxisloester.kotti_configure

        to enable the ``praxisloester`` add-on.

    :param settings: Kotti configuration dictionary.
    :type settings: dict
    """

    settings['pyramid.includes'] += ' praxisloester'
    settings['kotti.alembic_dirs'] += ' praxisloester:alembic'
    settings['kotti.available_types'] += ' praxisloester.resources.CustomContent'
    settings['kotti.fanstatic.view_needed'] += ' praxisloester.fanstatic.css_and_js'
    File.type_info.addable_to.append('CustomContent')


def includeme(config):
    """ Don't add this to your ``pyramid_includes``, but add the
    ``kotti_configure`` above to your ``kotti.configurators`` instead.

    :param config: Pyramid configurator object.
    :type config: :class:`pyramid.config.Configurator`
    """

    config.add_translation_dirs('praxisloester:locale')
    config.add_static_view('static-praxisloester', 'praxisloester:static')

    config.scan(__name__)
