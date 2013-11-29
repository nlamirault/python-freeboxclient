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


class ApiWifiTestCase(FreeboxOSClientTestCase):

    @responses.activate
    def test_get_wifi_status(self):
        responses.add(responses.GET,
                      '%s/%s/wifi' % (self.freebox_os_uri,
                                      self.freebox_os_api_version),
                      body="{ \"success\":true, \"result\":{ "
                      " \"detected\":true, \"bss\":{ "
                      " \"perso\":{ \"has_wps\":false, "
                      " \"bssid\":\"00:24:D4:DA:FF:7C\", \"name\":\"perso\", "
                      " \"active\":true }, "
                      " \"freewifi\":{ \"has_wps\":false, "
                      " \"bssid\":\"00:24:D4:DA:FF:7D\", "
                      " \"name\":\"freewifi\", "
                      " \"active\":true } }, \"active\":true } }",
                      status=200,
                      content_type='application/json')
        wifi = self.freebox_client.get_wifi_status()
        self.assertTrue(wifi['active'])
        self.assertTrue(wifi['bss'] is not None)

    @responses.activate
    def test_get_wifi_configuration(self):
        responses.add(responses.GET,
                      '%s/%s/wifi/config' % (self.freebox_os_uri,
                                             self.freebox_os_api_version),
                      body="{ \"success\":true, \"result\":{ "
                      " \"bss\":{ \"perso\":{ \"enabled\":true, "
                      " \"ssid\":\"Freebox-cafe\", "
                      "\"encryption\":\"wpa2_psk_ccmp\", "
                      " \"eapol_version\":2, "
                      " \"hide_ssid\":false, "
                      " \"mac_filter\":\"disabled\", "
                      " \"key\":\"etpuisquoiencore?\" } }, "
                      " \"ap_params\":{ \"enabled\":true, "
                      "\"ht_mode\":\"20\", \"channel\":3 } } }",
                      status=200,
                      content_type='application/json')
        wifi = self.freebox_client.get_wifi_config()
        self.assertTrue(wifi['ap_params'] is not None)
        self.assertTrue(wifi['bss'] is not None)

    @responses.activate
    def test_reset_wifi_config(self):
        responses.add(responses.POST,
                      '%s/%s/wifi/config/reset' %
                      (self.freebox_os_uri, self.freebox_os_api_version),
                      body="{ \"success\":true }",
                      status=200,
                      content_type='application/json')
        deleted = self.freebox_client.reset_wifi_config()
        self.assertTrue(deleted['success'])

    # @responses.activate
    # def test_get_wifi_stations(self):
    #     responses.add(responses.GET,
    #                   '%s/%s/wifi' % (self.freebox_os_uri,
    #                                   self.freebox_os_api_version),
    #                   body="",
    #                   status=200,
    #                   content_type='application/json')
    #     wifi = self.freebox_client.get_wifi_status()
    #     self.assertTrue(wifi['active'])
    #     self.assertTrue(wifi['bss'] is not None)
