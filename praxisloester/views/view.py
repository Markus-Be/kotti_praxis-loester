# -*- coding: utf-8 -*-

"""
Created on 2015-11-18
:author: markus (markus@terminal21.de)
"""

from pyramid.view import view_config
from pyramid.view import view_defaults

from praxisloester import _
from praxisloester.resources import CustomContent
from praxisloester.fanstatic import css_and_js
from praxisloester.views import BaseView


@view_defaults(context=CustomContent, permission='view')
class CustomContentViews(BaseView):
    """ Views for :class:`praxisloester.resources.CustomContent` """

    @view_config(name='view', permission='view',
                 renderer='praxisloester:templates/custom-content-default.pt')
    def default_view(self):
        """ Default view for :class:`praxisloester.resources.CustomContent`

        :result: Dictionary needed to render the template.
        :rtype: dict
        """

        return {
            'foo': _(u'bar'),
        }

    @view_config(name='alternative-view', permission='view',
                 renderer='praxisloester:templates/custom-content-alternative.pt')
    def alternative_view(self):
        """ Alternative view for :class:`praxisloester.resources.CustomContent`.
        This view requires the JS / CSS resources defined in
        :mod:`praxisloester.fanstatic`.

        :result: Dictionary needed to render the template.
        :rtype: dict
        """

        css_and_js.need()

        return {
            'foo': _(u'bar'),
        }
