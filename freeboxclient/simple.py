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


from freeboxclient import __author__, CONFIG_FILE
from freeboxclient.config import get_configuration_filename
from cliff.command import Command
import logging
from os.path import exists
import yaml


class About(Command):
    "A command that prints information about this tool."

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.app.stdout.write('This is a client for the Freebox OS.\n')
        self.app.stdout.write('Copyright (c) %s\n' % __author__)


class Configuration(Command):
    "A command that prints available configuration. "

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        #self.app.stdout.write('Configuration:' % CONFIG_FILE)
        config = load_configuration()
        if config:
        # if exists(config):
        #     f = open(config)
        #     settings = yaml.load(f)
            self.app.stdout.write("Configuration:\n%s" % config)
        else:
            self.app.stdout.write("Configuration file %s doesn't exists.\n" %
                                  config)
