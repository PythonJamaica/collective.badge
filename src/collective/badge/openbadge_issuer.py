# -*- coding: utf-8 -*-
import json
from Products.Five import BrowserView
from plone import api


class OpenBadgeIssuerJSON(BrowserView):

    def __call__(self):
        """return the issuer information based on openbadge spec"""
        portal = api.portal.get()
        name = portal.title
        url = portal.portal_url()
        description = portal.description
        email = api.portal.get_registry_record(name="plone.email_from_address")

        issuer = json.dumps({
                             'name': name,
                             'url': url,
                             'description': description,
                             'email': email
                             })
        return issuer
