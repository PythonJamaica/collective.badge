# -*- coding: utf-8 -*-
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import json


class OpenBadgeJSON(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        """Method to return the Badge Class as JSON"""
        self.context.id
        url = self.context.absolute_url()
        image = "%s/@@images/image/" % url
        name = self.context.title
        import pdb;pdb.set_trace()
        description = self.context.description
        criteria = self.context.text.output
        issuer = "%s/@@openbadge_issuer.json" % self.request['BASE1']
        badge = json.dumps({'name': name,
                            'criteria': criteria,
                            'issuer': issuer,
                            'image': image,
                            'description': description})
        return badge
