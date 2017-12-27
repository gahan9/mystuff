# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from builtins import object

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from future import standard_library

from .survey import Survey

standard_library.install_aliases()


class Response(models.Model):

    """
        A Response object is a collection of questions and answers with a
        unique interview uuid.
    """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    survey = models.ForeignKey(Survey, related_name="responses")
    user = models.ForeignKey(User, null=True, blank=True)
    interview_uuid = models.CharField(_(u"Interview unique identifier"),
                                      max_length=36)

    class Meta(object):
        verbose_name = _('response')
        verbose_name_plural = _('responses')

    def __str__(self):
        msg = u"Response to {} by {}".format(self.survey, self.user)
        msg += u" on {}".format(self.created)
        return msg
