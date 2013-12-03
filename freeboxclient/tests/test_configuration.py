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

import os
from os import path
import re
import time
import unittest

import freeboxclient
from freeboxclient import common
from freeboxclient import config


class FreeboxOSConfigurationTestCase(unittest.TestCase):

    def test_configuration_filename(self):
        filename = "%s/.config/freeboxos.yml" % path.expanduser("~")
        self.assertEqual(filename, config.get_configuration_filename())

    def test_load_configuration_when_file_doesnt_exists(self):
        freeboxclient.CONFIG_FILE = "/tmp/%s" % int(round(time.time() * 1000))
        self.assertRaises(common.FreeboxOSException,
                          config.load_configuration)

    def test_load_configuration(self):
        freeboxclient.CONFIG_FILE = "%s.yml" % int(round(time.time() * 1000))
        self._creates_configuration_file()
        conf = config.load_configuration()
        self.assertEqual('python-freeboxclient', conf['app_id'])
        self.assertEqual('Python-Freeboxclient', conf['app_name'])
        self.assertEqual('0.1.0', conf['app_version'])
        self.assertEqual('Python-Freeboxclient-Laptop', conf['device_name'])
        self._delete_configuration_file()

    def test_save_configuration_on_existing_file(self):
        freeboxclient.CONFIG_FILE = "%s.yml" % int(round(time.time() * 1000))
        self._creates_configuration_file()
        conf = config.load_configuration()
        conf['app_token'] = 'dyNYgfK0Ya'
        conf['track_id'] = '666'
        conf['status'] = 'granted'
        conf['challenge'] = 'Bj6xMqoe+DCHD44Kq'
        config_file = config.get_configuration_filename()
        config.save_configuration(conf)
        self.assertTrue('dyNYgfK0Ya' in open(config_file).read())
        self.assertTrue('666' in open(config_file).read())
        self.assertTrue('granted' in open(config_file).read())
        self.assertTrue('Bj6xMqoe+DCHD44Kq' in open(config_file).read())

    def _creates_configuration_file(self):
        output_file = "%s/.config/%s" % (path.expanduser("~"),
                                         freeboxclient.CONFIG_FILE)
        with open(output_file, 'w') as out:
            out.write("app_id: 'python-freeboxclient'\n")
            out.write("app_name: 'Python-Freeboxclient'\n")
            out.write("app_version: '0.1.0'\n")
            out.write("device_name: 'Python-Freeboxclient-Laptop'\n")

    def _delete_configuration_file(self):
        output_file = "%s/.config/%s" % (path.expanduser("~"),
                                         freeboxclient.CONFIG_FILE)
        os.remove(output_file)
