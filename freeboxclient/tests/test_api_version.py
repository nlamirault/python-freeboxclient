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


from freeboxclient.tests.commons import FreeboxOSClientTestCase
import responses


class ApiVersionTestCase(FreeboxOSClientTestCase):

    @responses.activate
    def test_get_version_without_auth(self):
        responses.add(responses.GET,
                      '%s/api_version' % self.freebox_os_uri,
                      body='{ "uid": "23b86ec8091013d668829fe12791fdab", "device_name": "Freebox Server", "api_version": "1.0", "api_base_url": "/api/", "device_type": "FreeboxServer1,1" }',
                      status=200,
                      content_type='application/json')
        version = self.freebox_client.version()
        # self.assertEquals("200", response.status_code)
         # self.assertEquals('application/json',
         #                   response.headers['Content-Type'])
        self.assertEqual('1.0', version['api_version'])
