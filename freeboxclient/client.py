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

from cliff.command import Command


logger = logging.getLogger(__name__)


class FreeboxCommand(Command):
    """Freebox command"""

    pass


class FreeboxApiVersion(FreeboxCommand):
    """ Retrieve the Freebox OS api version. """

    #log = logging.getLogger(__name__)
    #_freebox = FreeboxClient()

    # def get_parser(self, prog_name):
    #     parser = super(FreeboxCommand, self).get_parser(prog_name)
    #     parser.add_argument(
    #         'api_version',
    #         metavar='<api_version>',
    #         help='Display API version of the FreeboxOS')
    #     return parser

    def take_action(self, parsed_args):
        logger.info("[FreeboxCmd] API_Version")
        api_version = self.app.freebox_client.version()
        #print "Result: %s" % api_version
        self.app.stdout.write('FreeboxOS: %s\n' %
                              api_version['api_version'])


class FreeboxLogin(FreeboxCommand):
    """ Login to the Freebox OS. """

    def take_action(self, parsed_args):
        logger.info("[FreeboxCmd] Login")
        tokens = self.app.freebox_client.login()
        self.app.stdout.write('FreeboxOS: %s\n' %
                              tokens)
