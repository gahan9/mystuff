# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

import logging
import os
from builtins import object, open
from datetime import datetime

from django.conf import settings
from django.utils.text import slugify
from future import standard_library
from survey.models import Survey

standard_library.install_aliases()


LOGGER = logging.getLogger(__name__)


class Survey2X(object):

    """ Abstract class for Survey exporter. """

    def __init__(self, survey=None):
        self._check_survey(survey)
        self.survey = survey

    def _check_survey(self, survey):
        if not isinstance(survey, Survey):
            msg = "Expected Survey not '{}'".format(survey.__class__.__name__)
            raise TypeError(msg)

    def _get_X(self):
        return self.__class__.__name__.split("Survey2")[1].lower()

    def _get_X_dir(self):
        return os.path.join(settings.ROOT, self._get_X())

    def file_name(self):
        """ Return the csv file name for a Survey.

        :param Survey survey: The survey we're treating. """
        file_name = u"{}.{}".format(slugify(self.survey.name), self._get_X())
        path = os.path.join(self._get_X_dir(), file_name)
        return path

    def need_update(self):
        """ Does a file need an update ? """
        latest_answer_date = self.survey.latest_answer_date()
        try:
            # mtime : modification time of the file
            mtime = os.path.getmtime(self.file_name())
        except OSError:
            # If the file do not exist, we need to update it.
            return True
        if not latest_answer_date:
            # There isn't any responses so if the file is created its up to date
            return False
        mtime = datetime.fromtimestamp(mtime)
        mtime = mtime.replace(tzinfo=latest_answer_date.tzinfo)
        if latest_answer_date > mtime:
            # If the file was generated before the last answer, it needs update.
            return True
        return False

    def survey_to_x(self):
        """ Return a string that will be written into a file.

        :rtype String:
        """
        raise NotImplementedError("Please implement survey_to_x()")

    def generate_file(self):
        """ Generate a x file corresponding to a Survey. """

        LOGGER.debug("Exporting survey '%s' to %s", self.survey, self._get_X())
        try:
            with open(self.file_name(), "w") as f:
                f.write(self.survey_to_x())
            LOGGER.info("Wrote %s in %s", self._get_X(), self.file_name())
        except IOError as exc:
            msg = "Must fix {} ".format(self._get_X_dir())
            msg += "in order to generate {} : {}".format(self._get_X(), exc)
            raise IOError(msg)
