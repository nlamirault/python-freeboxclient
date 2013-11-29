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


from freeboxclient.api import FreeboxClient
import logging
import unittest


logger = logging.getLogger(__name__)


class FreeboxOSClientTestCase(unittest.TestCase):

    freebox_client = None
    freebox_os_uri = 'http://mafreebox.freebox.fr'
    freebox_os_api_version = 'api/v1'

    def setUp(self):
        self.freebox_client = FreeboxClient('python-freeboxclient-ut',
                                            'freeboxos-ut',
                                            '0.1.0',
                                            'MyFreebox')

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
        self.assertEquals(status, response.status_code)
        self.assertEquals('application/json',
                          response.headers["Content-Type"])
