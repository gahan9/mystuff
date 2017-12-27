# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

import os
import time

from django.conf import settings
from future import standard_library
from survey.exporter.survey2x import Survey2X
from survey.tests.management.test_management import TestManagement

standard_library.install_aliases()


class TestSurvey2X(TestManagement):

    def setUp(self):
        TestManagement.setUp(self)
        self.s2x = Survey2X(self.survey)

    def test_survey_2_x(self):
        self.assertRaises(NotImplementedError, self.s2x.survey_to_x)

    def test_need_update(self):
        class Survey2Survey(Survey2X):
            def survey_to_x(self):
                file_ = open(self.file_name(), "w")
                file_.write(".")
                file_.close()

        s2xi = Survey2Survey(self.survey)
        expected = os.path.join(settings.ROOT, "survey",
                                "test-management-survey.survey")
        self.assertEqual(s2xi.file_name(), expected)
        self.assertTrue(s2xi.need_update())
        s2xi.survey_to_x()
        self.assertFalse(s2xi.need_update())
        self.response.save()
        self.assertTrue(s2xi.need_update())
        if os.path.exists(expected):
            os.remove(expected)
