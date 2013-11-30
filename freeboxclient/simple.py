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

from cliff import command

import freeboxclient
from freeboxclient import config


class About(command.Command):
    """A command that prints information about this tool."""

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.app.stdout.write('This is a client for the Freebox OS.\n')
        self.app.stdout.write('Copyright (c) %s\n' % freeboxclient.__author__)


class Configuration(command.Command):
    """A command that prints available configuration."""

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        conf = config.load_configuration()
        if conf:
            self.app.stdout.write("Configuration:\n%s" % conf)
        else:
            self.app.stdout.write("Configuration file %s doesn't exists.\n" %
                                  config)
