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


class ApiCallsTestCase(FreeboxOSClientTestCase):

    @responses.activate
    def test_get_all_calls(self):
        responses.add(responses.GET,
                      '%s/%s/call/log' % (self.freebox_os_uri,
                                          self.freebox_os_api_version),
                      body="{ \"success\":true,"
                      " \"result\":[ "
                      "{ \"number\":\"0102030405\","
                      " \"type\":\"missed\", \"id\":69, \"duration\":1, "
                      "\"datetime\":1359546363, \"contact_id\":56, "
                      "\"line_id\":0, \"name\":\"r0ro (Freebox)\", "
                      "\"new\":true },"
                      " { \"number\":\"**1\", \"type\":\"outgoing\", "
                      "\"id\":68, \"duration\":5, \"datetime\":1359545960, "
                      "\"contact_id\":0, \"line_id\":0, \"name\":\"**1\", "
                      "\"new\":false } "
                      "] }",
                      status=200,
                      content_type='application/json')
        calls = self.freebox_client.get_calls()
        self.assertEqual(2, len(calls))

    @responses.activate
    def test_get_call(self):
        responses.add(responses.GET,
                      '%s/%s/call/log/69' % (self.freebox_os_uri,
                                             self.freebox_os_api_version),
                      body="{ \"success\":true, \"result\":{ "
                      " \"number\":\"0102030405\", \"type\":\"missed\", "
                      " \"id\":69, \"duration\":1, \"datetime\":1359546363, "
                      " \"contact_id\":56, \"line_id\":0, "
                      "\"name\":\"Romain Bureau\", \"new\":true } }",
                      status=200,
                      content_type='application/json')
        call = self.freebox_client.get_call('69')
        self.assertEqual('0102030405', call['number'])

    @responses.activate
    def test_delete_call(self):
        responses.add(responses.DELETE,
                      '%s/%s/call/log/69' % (self.freebox_os_uri,
                                             self.freebox_os_api_version),
                      body="{ \"success\":true }",
                      status=200,
                      content_type='application/json')
        deleted = self.freebox_client.delete_call('69')
        self.assertTrue(deleted['success'])
