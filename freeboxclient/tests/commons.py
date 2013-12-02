#
# Copyright 2013 Nicolas Lamirault <nicolas.lamirault@gmail.com>.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#


import logging
import unittest

from freeboxclient import api


logger = logging.getLogger(__name__)


class FreeboxOSClientTestCase(unittest.TestCase):

    freebox_client = None
    freebox_os_uri = 'http://mafreebox.freebox.fr'
    freebox_os_api_version = 'api/v1'

    def setUp(self):
        conf = {}
        conf['app_id'] = 'python-freeboxclient'
        conf['app_name'] = 'Python-Freeboxclient'
        conf['app_version'] = '0.1.0'
        conf['device_name'] = 'Python-Freeboxclient-Laptop'
        self.freebox_client = api.FreeboxClient(conf)

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        logger.info("Start unit tests")

    @classmethod
    def tearDownClass(cls):
        pass

    def check_code_and_content_type(self, response, status):
        #logger.info("Response: %s" % response)
        self.assertEqual(status, response.status_code)
        self.assertEqual('application/json',
                         response.headers["Content-Type"])
