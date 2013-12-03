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

import time
import unittest

import responses

import freeboxclient
from freeboxclient import common
from freeboxclient import config
from freeboxclient.tests import commons


class ApiAuthTestCase(commons.FreeboxOSClientTestCase):

    def test_check_authorization_when_no_authorization_request_sent(self):
        self.assertRaises(common.FreeboxOSException,
                          self.freebox_client.check_authorization)

    @responses.activate
    def test_check_authorization_with_valid_configuration(self):
        self.freebox_client.track_id = '42'
        responses.add(responses.GET,
                      '%s/%s/login/authorize/42' %
                      (self.freebox_os_uri,
                       self.freebox_os_api_version),
                      body="{ \"success\":true, \"result\":{ "
                      "\"status\":\"pending\", "
                      "\"challenge\":\"Bj6xMqoe+DCHD44KqBljJ579seOXNWr2\" "
                      "} }",
                      status=200,
                      content_type='application/json')
        response = self.freebox_client.check_authorization()
        self.assertTrue("pending", response['status'])

    @unittest.skip("Find JSON response")
    def test_check_authorization_with_invalid_track_id(self):
        self.freebox_client.track_id = '00'
        response = self.freebox_client.check_authorization()

    @responses.activate
    def test_ask_authorization(self):
        freeboxclient.CONFIG_FILE = self.random_configuration_file()
        self.creates_configuration_file()
        config_file = config.get_configuration_filename()
        self.assertFalse('999' in open(config_file).read())
        self.assertFalse('dyNYgfK0Ya6FW' in open(config_file).read())
        responses.add(responses.POST,
                      '%s/%s/login/authorize' %
                      (self.freebox_os_uri,
                       self.freebox_os_api_version),
                      body="{ \"success\":true, \"result\":{ "
                      "\"app_token\":\"dyNYgfK0Ya6FW\", "
                      "\"track_id\":999 "
                      "} }",
                      status=200,
                      content_type='application/json')
        response = self.freebox_client.ask_authorization()
        self.assertTrue('999' in open(config_file).read())
        self.assertTrue('dyNYgfK0Ya6FW' in open(config_file).read())

    @responses.activate
    def test_freeboxos_login(self):
        self.freebox_client.track_id = '999'
        self.freebox_client.app_token = 'dyNYgfK0Ya6FW'
        freeboxclient.CONFIG_FILE = self.random_configuration_file()
        self.creates_configuration_file()
        config_file = config.get_configuration_filename()
        responses.add(responses.GET,
                      '%s/%s/login' %
                      (self.freebox_os_uri,
                       self.freebox_os_api_version),
                      body="{ \"success\":true, \"result\":{ "
                      "\"logged_in\":false, "
                      "\"challenge\":\"VzhbtpR4r8CLaJle2\" "
                      "} }",
                      status=200,
                      content_type='application/json')
        response = self.freebox_client.login()
        self.assertTrue('VzhbtpR4r8CLaJle2' in open(config_file).read())
