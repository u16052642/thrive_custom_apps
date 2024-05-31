# Copyright 2015-2016 Camptocamp SA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)

# pylint: disable=thrive-addons-relative-import
# we are testing, we want to test as we were an external consumer of the API
from thrive.addons.queue_job.jobrunner import channels

from .common import load_doctests

load_tests = load_doctests(channels)
