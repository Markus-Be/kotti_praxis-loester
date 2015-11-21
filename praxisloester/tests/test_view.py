# -*- coding: utf-8 -*-

"""
Created on 2015-11-18
:author: markus (markus@terminal21.de)
"""

from pytest import fixture


@fixture
def dummy_content(root):

    from praxisloester.resources import CustomContent

    root['cc'] = cc = CustomContent(
        title=u'My content',
        description=u'My very custom content is custom',
        custom_attribute='Lorem ipsum'
    )

    return cc


def test_view(dummy_content, dummy_request):

    from praxisloester.views.view import CustomContentViews

    views = CustomContentViews(dummy_content, dummy_request)

    default = views.default_view()
    assert 'foo' in default

    alternative = views.alternative_view()
    assert alternative['foo'] == u'bar'
